from pathlib import Path


path = Path("/home/baiheng/raspa_debug_instrumented_src/src/matrix.c")
text = path.read_text()

text = text.replace(
    '#include <math.h>\n#include "matrix.h"',
    '#include <math.h>\n'
    '#include <string.h>\n'
    '#include <time.h>\n'
    '#include <unistd.h>\n'
    '#include <sys/stat.h>\n'
    '#include <sys/types.h>\n'
    '#include <execinfo.h>\n'
    '#include "matrix.h"',
)

helpers = r'''
static long RASPA_GJ_DEBUG_CALL_ID=0;

static void RASPA_GJ_MkdirIfNeeded(const char *path)
{
  struct stat st;
  if(stat(path,&st)!=0) mkdir(path,0777);
}

static void RASPA_GJ_MkdirP(const char *path)
{
  char buffer[4096];
  char *p;
  size_t len;

  if(path==NULL) return;
  len=strlen(path);
  if(len==0 || len>=sizeof(buffer)) return;
  strcpy(buffer,path);
  if(buffer[len-1]=='/') buffer[len-1]='\0';
  for(p=buffer+1;*p;p++)
  {
    if(*p=='/')
    {
      *p='\0';
      RASPA_GJ_MkdirIfNeeded(buffer);
      *p='/';
    }
  }
  RASPA_GJ_MkdirIfNeeded(buffer);
}

static REAL** RASPA_GJ_CopyMatrix(REAL_MATRIX x,int rows,int cols)
{
  int i,j;
  REAL **copy;

  copy=(REAL**)calloc(rows,sizeof(REAL*));
  if(copy==NULL) return NULL;
  for(i=0;i<rows;i++)
  {
    copy[i]=(REAL*)calloc(cols,sizeof(REAL));
    if(copy[i]==NULL) return copy;
    for(j=0;j<cols;j++) copy[i][j]=x.element[i][j];
  }
  return copy;
}

static void RASPA_GJ_FreeMatrixCopy(REAL **x,int rows)
{
  int i;

  if(x==NULL) return;
  for(i=0;i<rows;i++) free(x[i]);
  free(x);
}

static void RASPA_GJ_DumpCopyCSV(const char *path,REAL **x,int rows,int cols)
{
  int i,j;
  FILE *file;

  file=fopen(path,"w");
  if(file==NULL || x==NULL) return;
  for(i=0;i<rows;i++)
  {
    for(j=0;j<cols;j++)
    {
      if(j>0) fprintf(file,",");
      fprintf(file,"%.17g",(double)x[i][j]);
    }
    fprintf(file,"\n");
  }
  fclose(file);
}

static void RASPA_GJ_DumpLiveCSV(const char *path,REAL_MATRIX x,int rows,int cols)
{
  int i,j;
  FILE *file;

  file=fopen(path,"w");
  if(file==NULL) return;
  for(i=0;i<rows;i++)
  {
    for(j=0;j<cols;j++)
    {
      if(j>0) fprintf(file,",");
      fprintf(file,"%.17g",(double)x.element[i][j]);
    }
    fprintf(file,"\n");
  }
  fclose(file);
}

static void RASPA_GJ_DumpBacktrace(const char *path)
{
  void *frames[128];
  int nframes;
  FILE *file;

  file=fopen(path,"w");
  if(file==NULL) return;
  nframes=backtrace(frames,128);
  backtrace_symbols_fd(frames,nframes,fileno(file));
  fclose(file);
}

static void RASPA_GJ_DumpSingularEvidence(long call_id,int iteration_i,int irow,int icol,
                                          REAL pivot_value,int n,int m,REAL_MATRIX a,
                                          REAL **a_original,REAL **b_original,
                                          const char *pivot_trace)
{
  char dir[4096],path[4096];
  const char *base;
  FILE *file;
  time_t now;

  base=getenv("RASPA_GJ_DEBUG_DIR");
  if(base==NULL || strlen(base)==0) base="gaussjordan_debug";
  snprintf(dir,sizeof(dir),"%s/singular_call_%ld",base,call_id);
  RASPA_GJ_MkdirP(dir);

  snprintf(path,sizeof(path),"%s/A_original.csv",dir);
  RASPA_GJ_DumpCopyCSV(path,a_original,n,n);
  snprintf(path,sizeof(path),"%s/A_at_failure.csv",dir);
  RASPA_GJ_DumpLiveCSV(path,a,n,n);
  snprintf(path,sizeof(path),"%s/B_original.csv",dir);
  RASPA_GJ_DumpCopyCSV(path,b_original,n,m);
  snprintf(path,sizeof(path),"%s/pivot_trace.csv",dir);
  file=fopen(path,"w");
  if(file!=NULL)
  {
    fprintf(file,"iteration_i,irow,icol,pivot_before_row_swap,big\n%s",pivot_trace);
    fclose(file);
  }
  now=time(NULL);
  snprintf(path,sizeof(path),"%s/metadata.json",dir);
  file=fopen(path,"w");
  if(file!=NULL)
  {
    fprintf(file,"{\n");
    fprintf(file,"  \"call_id\": %ld,\n",call_id);
    fprintf(file,"  \"iteration_i\": %d,\n",iteration_i);
    fprintf(file,"  \"irow\": %d,\n",irow);
    fprintf(file,"  \"icol\": %d,\n",icol);
    fprintf(file,"  \"pivot_value\": %.17g,\n",(double)pivot_value);
    fprintf(file,"  \"n\": %d,\n",n);
    fprintf(file,"  \"m\": %d,\n",m);
    fprintf(file,"  \"timestamp_unix\": %ld,\n",(long)now);
    fprintf(file,"  \"diagnostic_exit_code\": 77\n");
    fprintf(file,"}\n");
    fclose(file);
  }
  snprintf(path,sizeof(path),"%s/BACKTRACE.txt",dir);
  RASPA_GJ_DumpBacktrace(path);
}

'''

text = text.replace('#include "utils.h"\n\n// Matrices are stored', '#include "utils.h"\n\n' + helpers + '// Matrices are stored')
text = text.replace(
    "  REAL big,dum,pivinv,temp;\n\n  indxc=(int*)calloc(n,sizeof(int));",
    "  REAL big,dum,pivinv,temp;\n"
    "  long call_id;\n"
    "  REAL **a_original;\n"
    "  REAL **b_original;\n"
    "  char pivot_trace[65536];\n"
    "  size_t pivot_trace_len;\n\n"
    "  indxc=(int*)calloc(n,sizeof(int));",
)
text = text.replace(
    "  ipiv=(int*)calloc(n,sizeof(int));\n\n  icol=irow=0;",
    "  ipiv=(int*)calloc(n,sizeof(int));\n"
    "  call_id=++RASPA_GJ_DEBUG_CALL_ID;\n"
    "  a_original=RASPA_GJ_CopyMatrix(a,n,n);\n"
    "  b_original=RASPA_GJ_CopyMatrix(b,n,m);\n"
    "  pivot_trace_len=0;\n"
    "  pivot_trace[0]='\\0';\n\n"
    "  icol=irow=0;",
)
text = text.replace(
    "    ++(ipiv[icol]);\n",
    "    if(pivot_trace_len<sizeof(pivot_trace))\n"
    "      pivot_trace_len+=(size_t)snprintf(pivot_trace+pivot_trace_len,sizeof(pivot_trace)-pivot_trace_len,\n"
    "                                        \"%d,%d,%d,%.17g,%.17g\\n\",\n"
    "                                        i,irow,icol,(double)a.element[irow][icol],(double)big);\n\n"
    "    ++(ipiv[icol]);\n",
    1,
)
text = text.replace(
    '      fprintf(stderr, "Matrix Inversion, Gauss-Jordan: Singular Matrix\\n");\n    }',
    '      fprintf(stderr, "Matrix Inversion, Gauss-Jordan: Singular Matrix\\n");\n'
    '      RASPA_GJ_DumpSingularEvidence(call_id,i,irow,icol,a.element[icol][icol],\n'
    '                                    n,m,a,a_original,b_original,pivot_trace);\n'
    '      RASPA_GJ_FreeMatrixCopy(a_original,n);\n'
    '      RASPA_GJ_FreeMatrixCopy(b_original,n);\n'
    '      free(ipiv); free(indxr); free(indxc);\n'
    '      exit(77);\n'
    '    }',
    1,
)
text = text.replace(
    "  free(ipiv);\n  free(indxr);",
    "  free(ipiv);\n"
    "  RASPA_GJ_FreeMatrixCopy(a_original,n);\n"
    "  RASPA_GJ_FreeMatrixCopy(b_original,n);\n"
    "  free(indxr);",
    1,
)

path.write_text(text)
