class AndroidEmulator:
    """
    模拟器窗口，请用纯黑背景
    """
    def __init__(self):
        self.origin = (844, 47)
        self.buttons = {
            'menu': (325, 730),             # 菜单按钮
            'home': (195, 730),             # 主页按钮
            'return': (65, 730),            # 返回按钮
        }

        self.apps = {
            'contacts': (150, 660),         # 联系人
            'msg-link': (65, 515),          # 获取短信内容的链接
        }

        self.app_buttons = {
            'contacts': {
                'me': (100, 480),
                'contact_sms': (350, 515),  # 联系人详情里面的短信按钮
            },
            'sms': {
                'add': (288, 672),
                'input': (180, 680),        # 短信输入框
                'copy': (50, 615),          # 弹出来的复制按钮
                'send': (355, 685),         # 发送按钮
            },
            'msg-link': {
                'pos': (5, 110),            # 网页第一个字符的位置
                'select-all': (120, 210),   # 全选按钮
                'copy': (190, 210),         # 复制
            }
        }

    def click_button(self, button):
        x, y = self.buttons[button]
        pyautogui.moveTo(x, y)
        pyautogui.click()

    def click_app(self, app):
        x, y = self.apps[app]
        pyautogui.moveTo(x, y)
        pyautogui.click()

    def click_app_button(self, app, button):
        x, y = self.app_buttons[app][button]
        pyautogui.moveTo(x, y)
        pyautogui.click()

    def send_message(self, text):
        self.click_button('home')
        self.click_app('sms')
        self.click_app_button('sms', 'edit')
        self.click_app_button('sms', 'input_field')


        # pyautogui.typewrite('Hello world!')

        self.click_app_button('sms', 'send')


if __name__ == '__main__':
    pass
