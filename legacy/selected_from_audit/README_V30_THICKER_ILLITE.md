# V30：在 RAW 最终干酪根板下方增加更厚的伊利石

## 固定输入
仅读取：

`KEROGEN_ONLY_FINALS/RAW_KEEP_COORDINATES/{case}_kerogen_only_raw_from_final.gro`

例如：

- `RMS_0p000_kerogen_only_raw_from_final.gro`
- `RMS_0p300_kerogen_only_raw_from_final.gro`
- `RMS_0p600_kerogen_only_raw_from_final.gro`
- `RMS_0p900_kerogen_only_raw_from_final.gro`

## 与 V29 的唯一本质区别

- V29：`illite_repeat_z = 1`
- V30：`illite_repeat_z = 2`

即伊利石沿 z 方向复制 2 个完整晶胞，厚度约为 V29 的 2 倍。

## 不改变干酪根

V30 仍严格保持：

- 不翻转
- 不居中
- 不平移
- 不 wrap
- 不标准化
- 不裁剪
- 不改变原子顺序
- 不改变任意干酪根坐标

程序仍检查 `kerogen_max_abs_coordinate_change_nm = 0.0`。

## X/Y 尺寸不变

V30 保留 V29 的紧凑 x/y 逻辑：

- `illite_xy_fit_mode = inside`
- 不因为增厚而扩大伊利石长宽
- 只增加 z 向厚度

## 运行

全部四组：

`39_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ALL.bat`

单组测试，例如 300：

`40_BUILD_THICKER_ILLITE_BELOW_RAW_FINAL_KEROGEN_ONE.bat RMS_0p300`

## 输出

`ILLITE_BELOW_RAW_FINAL_KEROGEN_V30_THICKER/`

## 注意

如果原始 RAW 干酪根板的最低 z 坐标太低，2 层伊利石可能没有足够空间放在其下方。V30 不会移动干酪根来腾空间，而会直接报错。此时不要改干酪根坐标；可将 `illite_repeat_z` 改回 1，或另行建立更大下部真空层的模拟盒。
