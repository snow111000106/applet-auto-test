# 需要把以下代码放入.\cmm-xhs-auto-miniprogram\venv\Lib\site-packages\minium\framework\minitest.py文件中
def assertMultiIn(self, first, second, msg=None):
    """
    自定义的断言方法，判断first里面有一个在second里面即通过
    """
    for i in first:
        if i in second:
            # 只要有一个元素在 second 中，断言通过
            return
    # 如果循环完毕都没有通过，则表示所有元素都不在 second 里面，断言失败
    standard_msg = f"列表 {first} 中的所有元素都不在列表 {second} 里面"
    self.fail(self._formatMessage(msg, standard_msg))