# DSGO APP Agent Test Brief Template

## Standard Brief

```text
测试目标：
- 只通过安卓 APP Agent 生成/修复：是/否
- 用户目标：
- 最终结论：

环境：
- 分支：
- APK 构建/安装命令：
- 设备：
- adb reverse：
- 后端/API 检查：

Agent 轮次：
1. 轮次名称
   - APP 输入意图：
   - task id：
   - 结果：
   - 问题：
   - 下一步：

产品链路修复：
- 文件：
- 原因：
- 验证：

运行验证：
- 截图：
- 日志：
- 是否连续更新：
- 是否可触控：
- 是否符合手机操作：

残余风险：
- 
```

## Gravity Tetris Baseline From 2026-05-20

This baseline is an example of the expected level of detail. Do not assume future tests have the same failures.

Goal: use the Android APP Agent to generate a playable gravity Tetris game where blocks are affected by gravity instead of snapping perfectly grid-by-grid.

APP Agent rounds:

1. Initial generation
   - Prompt intent: create playable gravity Tetris with acceleration, touch controls, and fast drop.
   - Result: Agent created project files.
   - Problem: save/result collection reported an empty change set.
   - Product fix: client fallback collected generated files through embedded Dora `/list` and `/read`.

2. Unsupported DrawNode rectangle API
   - Problem: Android runtime error for `drawRect`.
   - APP Agent repair: replace rectangles with `drawPolygon`.
   - Result: build passed, next runtime error appeared.

3. Unsupported DrawNode line API
   - Problem: Android runtime error for `drawLine`.
   - APP Agent repair: replace lines with `drawSegment`.
   - Result: game rendered, but active piece did not continue falling.

4. Incorrect schedule semantics
   - Problem: product prompt said `return true` keeps scheduling alive, but Dora docs say `return true` stops scheduling; `return false`/nil continues.
   - Product fix: update Agent constraints and validation.
   - APP Agent repair: change main loop to return false.
   - Result: the game updated continuously, but a piece could still hover after landing.

5. Fractional grid indexing
   - Problem: fractional physics position was used in grid collision checks.
   - Product fix: add Agent constraint to floor/convert grid row/column indices before indexing.
   - APP Agent repair: use integer collision rows.
   - Result: runtime became stable but landing logic still needed repair.

6. Landing/locking logic
   - Problem: when a piece could not fall further, generated code only set velocity to zero and left the active piece stuck.
   - Product fix: add Agent constraint that falling-block games must lock, clear lines, and spawn next piece.
   - APP Agent repair: lock landed pieces and spawn the next active piece.
   - Result: screenshots several seconds apart showed changing board state, locked blocks, and new pieces falling.

Final evidence:

- Type check: `npm --prefix frontend exec tsc -- -p frontend/tsconfig.json --noEmit` passed.
- Build/install: `local/dev/start-android.ps1` passed and installed the APK.
- APP-generated result screenshots:
  - `local/tmp/dsgo-gravity-lock-run-mid.png`
  - `local/tmp/dsgo-gravity-lock-run-later.png`

Phone suitability conclusion:

- Core loop became playable on Android: visible portrait board, continuous falling, locking, new piece spawn, and touch zones displayed.
- It was suitable as a functional phone prototype, not as a polished final mobile game UI. The runtime briefly exposing Dora Dev UI indicated an APP/run-path integration risk that should be separately tightened before release.
