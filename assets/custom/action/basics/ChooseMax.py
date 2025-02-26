from maa.context import Context
from maa.custom_action import CustomAction
import time

    
class ChooseMax(CustomAction):
    # 识别当前物品，再点击物品
    def run(
        self, context: Context, argv: CustomAction.RunArg
    ) -> CustomAction.RunResult:
        image = context.tasker.controller.post_screencap().wait().get()
        # 仙人掌能量棒棒糖
        hp = context.run_recognition("Station_hp", image)
        if hp:
            x,y = (
                hp.best_result.box[0] + hp.best_result.box[2] // 2,
                hp.best_result.box[1] + hp.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()  # 点击物品
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()  # 最多
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(269,510).wait()  # 取消
            time.sleep(1)
            return CustomAction.RunResult(success=True)
        # 提神棒棒糖
        mp = context.run_recognition("Station_mp", image)
        if mp:
            x,y = (
                mp.best_result.box[0] + mp.best_result.box[2] // 2,
                mp.best_result.box[1] + mp.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(269,510).wait()
            time.sleep(1)
            image = context.tasker.controller.post_screencap().wait().get()
        # 进货采买书    
        book = context.run_recognition("Station_w_book", image)
        if book:
            x,y = (
                book.best_result.box[0] + book.best_result.box[2] // 2,
                book.best_result.box[1] + book.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(269,510).wait()
            time.sleep(1)
            image = context.tasker.controller.post_screencap().wait().get()
        # 月协议
        m_agreement = context.run_recognition("Station_m_agreement", image)
        if m_agreement:
            x,y = (
                m_agreement.best_result.box[0] + m_agreement.best_result.box[2] // 2,
                m_agreement.best_result.box[1] + m_agreement.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(269,510).wait()
            time.sleep(1)
            image = context.tasker.controller.post_screencap().wait().get()
        # 周协议
        w_agreement = context.run_recognition("Station_w_agreement", image)
        if w_agreement:
            x,y = (
                w_agreement.best_result.box[0] + w_agreement.best_result.box[2] // 2,
                w_agreement.best_result.box[1] + w_agreement.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(269,510).wait()
            time.sleep(1)
            image = context.tasker.controller.post_screencap().wait().get()
        # 日桦石
        stone = context.run_recognition("Station_stone", image)
        if stone:
            x,y = (
                stone.best_result.box[0] + stone.best_result.box[2] // 2,
                stone.best_result.box[1] + stone.best_result.box[3] // 2,
            )
            context.tasker.controller.post_click(x, y).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(888,380).wait()
            time.sleep(1)
            context.tasker.controller.post_click(269,510).wait()
            time.sleep(1)
            image = context.tasker.controller.post_screencap().wait().get()

        return CustomAction.RunResult(success=True)
