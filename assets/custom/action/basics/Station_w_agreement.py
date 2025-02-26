from maa.context import Context
from maa.custom_action import CustomAction
import time

    
class Station_w_agreement(CustomAction):
    # 识别当前物品，再点击物品
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult:
        image = context.tasker.controller.post_screencap().wait().get()
        w_agreement = context.run_recognition("Station_w_agreement", image)
        if w_agreement:
            x,y = (
                w_agreement.best_result.box[0] + w_agreement.best_result.box[2] // 2,
                w_agreement.best_result.box[1] + w_agreement.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()
            time.sleep(2)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(2)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(2)
            context.tasker.controller.post_click(269,510).wait()
            time.sleep(1)
            image = context.tasker.controller.post_screencap().wait().get()