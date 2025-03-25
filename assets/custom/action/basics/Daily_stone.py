from maa.context import Context
from maa.custom_action import CustomAction
import time

    
class Daily_stone(CustomAction):
    # 识别当前物品，再点击物品
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult:
        image = context.tasker.controller.post_screencap().wait().get()
        stone = context.run_recognition("Dailystone", image)
        if stone:
            x,y = (
                stone.best_result.box[0] + stone.best_result.box[2] // 2,
                stone.best_result.box[1] + stone.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()
            time.sleep(2)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(2)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(900,520).wait()  # 确定
            time.sleep(1)
            # context.tasker.controller.post_click(270,510).wait()  # 取消
            # time.sleep(1)
            context.tasker.controller.post_click(690,160).wait()  # 获得物品
            time.sleep(1)
            image = context.tasker.controller.post_screencap().wait().get()
            context.run_pipeline(entry="BlackShop")
        return CustomAction.RunResult(success=True)