from maa.context import Context
from maa.custom_action import CustomAction
import time

    
class Daily_tape(CustomAction):
    # 识别当前物品，再点击物品
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult:
        image = context.tasker.controller.post_screencap().wait().get()
        time.sleep(2)
        tape = context.run_recognition("Dailytape", image)
        if tape:
            x,y = (
                tape.best_result.box[0] + tape.best_result.box[2] // 2,
                tape.best_result.box[1] + tape.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()
            time.sleep(2)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(900,520).wait()
            time.sleep(1)
            context.tasker.controller.post_click(690,160).wait()
            time.sleep(2)
            image = context.tasker.controller.post_screencap().wait().get()
            context.run_pipeline(entry="BlackShop")
        return CustomAction.RunResult(success=True)