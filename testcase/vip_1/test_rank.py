
import minium, time
from conf import config, route
from minium import Callback
from testcase.vip_1.BaseCase import BaseCase
from page.RankPage import RankPage
from common.base import Base


#@minium.skipUnless(condition=config.platform != "ios", reason="仅ios无vip页面")
@minium.ddt_class
class RankPageTest(BaseCase):

    rankpage = None

    def __init__(self, methodName='runTest'):
        super(RankPageTest, self).__init__(methodName)
        self.rankpage = RankPage(self)

    @classmethod
    def setUpClass(cls):
        super(RankPageTest, cls).setUpClass()
        cls.rankpage = RankPage(cls)
        cls.rankpage.into_rank_page()



    @minium.ddt_case("fans","industry","area","mcn")
    def test_vip1_author_rank(self,vaule):
        """测试普通会员时的博主相关榜单"""
        detail_rank=vaule
        
        self.rankpage.switch_rank(rank_type="author")
        self.rankpage.switch_detail_rank(rank_type="author",detail_type=detail_rank)

        self.rankpage.scroll_page(high=600,duration=1000)
        time.sleep(0.5)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())

        for i in range(2): 
            self.rankpage.get_element(self.rankpage.open_date_choice).click()
            time.sleep(0.3)
            self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
            time.sleep(0.5)
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
                self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            time.sleep(0.5)
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
            self.assertEqual(True,self.rankpage.is_have_upgrade())

        self.rankpage.get_element(self.rankpage.open_date_choice).click()
        time.sleep(0.3)
        self.rankpage.get_element(self.rankpage.pop_item_select).move(0,80,200)
        time.sleep(0.5)
        self.rankpage.get_element(self.rankpage.pop_yes_button).click()
        if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()



        if detail_rank=="fans" or detail_rank=="industry":
            self.rankpage.get_element(self.rankpage.author_category_choice).click()
            self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
            self.rankpage.get_element(self.rankpage.pop_yes_button).click() 
            time.sleep(0.3)
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
            self.assertEqual(True,self.rankpage.is_have_upgrade())

        elif detail_rank=="area":
            self.rankpage.get_element(self.rankpage.author_city_choice).click()
            self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
            self.rankpage.get_element(self.rankpage.pop_yes_button).click() 
            time.sleep(0.3)
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
            self.assertEqual(True,self.rankpage.is_have_upgrade())

    @minium.ddt_case("realtime","business","low_fans")
    def test_vip1_note_rank(self,vaule):
        """测试普通会员时的笔记相关榜单"""
        detail_rank=vaule

        self.rankpage.switch_rank(rank_type="note")
        self.rankpage.switch_detail_rank(rank_type="note",detail_type=detail_rank)        

        self.rankpage.scroll_page(high=950,duration=1000)
        time.sleep(0.5)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())

        if detail_rank=="realtime":
            open_pop_time=self.rankpage.note_realtime_open_time_choice
            item_num=3
        elif detail_rank=="business":
            open_pop_time=self.rankpage.open_date_choice
            item_num=2
        else:
            open_pop_time=self.rankpage.note_low_fans
            item_num=3

        for i in range(item_num): 
            self.rankpage.get_element(open_pop_time).click()
            time.sleep(0.3)
            self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
            time.sleep(0.5)
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
                self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            time.sleep(0.5)
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))   
            self.assertEqual(True,self.rankpage.is_have_upgrade())

        self.rankpage.get_element(open_pop_time).click()
        time.sleep(0.3)
        self.rankpage.get_element(self.rankpage.pop_item_select).move(0,item_num*40,200)
        time.sleep(0.5)
        self.rankpage.get_element(self.rankpage.pop_yes_button).click()
        if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()


        self.rankpage.get_element(self.rankpage.note_open_category_choice).click()
        self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
        self.rankpage.get_element(self.rankpage.pop_yes_button).click() 
        time.sleep(0.3)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())



    @minium.ddt_case("business","recommend","launch")
    def test_vip1_brand_rank(self,vaule):
        """测试普通会员时的品牌相关榜单"""
        detail_rank=vaule

        self.rankpage.switch_rank(rank_type="brand")
        self.rankpage.switch_detail_rank(rank_type="brand",detail_type=detail_rank)        

        self.rankpage.scroll_page(high=600,duration=1000)
        time.sleep(0.5)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())

        if detail_rank=="launch":
            item_num=1
        else:
            item_num=2

        for i in range(item_num): 
            self.rankpage.get_element(self.rankpage.open_date_choice).click()
            time.sleep(0.3)
            self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
            time.sleep(0.5)
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
                self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            time.sleep(0.5)
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))   
            self.assertEqual(True,self.rankpage.is_have_upgrade())

        self.rankpage.get_element(self.rankpage.open_date_choice).click()
        time.sleep(0.3)
        self.rankpage.get_element(self.rankpage.pop_item_select).move(0,item_num*40,200)
        time.sleep(0.5)
        self.rankpage.get_element(self.rankpage.pop_yes_button).click()
        if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()


        self.rankpage.get_element(self.rankpage.brand_open_category_choice).click()
        self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
        self.rankpage.get_element(self.rankpage.pop_yes_button).click() 
        time.sleep(0.3)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())



    @minium.ddt_case("business","recommend","launch")
    def test_vip1_kind_rank(self,vaule):
        """测试普通会员时的品类相关榜单"""
        detail_rank=vaule

        self.rankpage.switch_rank(rank_type="kind")
        self.rankpage.switch_detail_rank(rank_type="kind",detail_type=detail_rank)        

        self.rankpage.scroll_page(high=600,duration=1000)
        time.sleep(0.5)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())

        if detail_rank=="launch":
            item_num=1
        else:
            item_num=2

        for i in range(item_num): 
            self.rankpage.get_element(self.rankpage.open_date_choice).click()
            time.sleep(0.3)
            self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
            time.sleep(0.5)
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
                self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            time.sleep(0.5)
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
            # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))   
            self.assertEqual(True,self.rankpage.is_have_upgrade())

        self.rankpage.get_element(self.rankpage.open_date_choice).click()
        time.sleep(0.3)
        self.rankpage.get_element(self.rankpage.pop_item_select).move(0,item_num*40,200)
        time.sleep(0.5)
        self.rankpage.get_element(self.rankpage.pop_yes_button).click()
        if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()


        self.rankpage.get_element(self.rankpage.kind_open_category_choice).click()
        self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
        self.rankpage.get_element(self.rankpage.pop_yes_button).click() 
        time.sleep(0.3)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())


    @minium.ddt_case("inc","total")
    def test_vip1_hot_key_rank(self,vaule):
        """测试普通会员时的热搜词相关榜单"""
        detail_rank=vaule

        self.rankpage.switch_rank(rank_type="hot_key")
        self.rankpage.switch_detail_rank(rank_type="hot_key",detail_type=detail_rank)        

        self.rankpage.scroll_page(high=600,duration=1000)
        time.sleep(0.5)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())

        if detail_rank=="inc":
            item_num=1
    
            for i in range(item_num): 
                self.rankpage.get_element(self.rankpage.open_date_choice).click()
                time.sleep(0.3)
                self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
                time.sleep(0.5)
                self.rankpage.get_element(self.rankpage.pop_yes_button).click()
                if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
                    self.rankpage.get_element(self.rankpage.pop_yes_button).click()
                time.sleep(0.5)
                # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
                # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))   
                self.assertEqual(True,self.rankpage.is_have_upgrade())


            self.rankpage.get_element(self.rankpage.open_date_choice).click()
            time.sleep(0.3)
            self.rankpage.get_element(self.rankpage.pop_item_select).move(0,item_num*40,200)
            time.sleep(0.5)
            self.rankpage.get_element(self.rankpage.pop_yes_button).click()
            if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
                self.rankpage.get_element(self.rankpage.pop_yes_button).click()
        else:
            pass


        self.rankpage.get_element(self.rankpage.hot_key_open_category_choice).click()
        self.rankpage.get_element(self.rankpage.pop_item_select).move(0,-40,200)
        self.rankpage.get_element(self.rankpage.pop_yes_button).click() 
        time.sleep(0.3)
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
        # self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))
        self.assertEqual(True,self.rankpage.is_have_upgrade())




    # @minium.ddt_case(("author","fans"),("author","industry"),("author","area"),("author","mcn"),
    #                  ("note","realtime"),("note","business"),("note","low_fans"),
    #                  ("brand","business"),("brand","recommend"),("brand","launch"),
    #                  ("kind","business"),("kind","recommend"),("kind","launch"),
    #                  ("hot_key","inc"),("hot_key","total"))
    # def test_vip1_rank(self,value):

    #     """测试普通会员各个榜单只能查看日榜的十条数据"""

    #     big_rank,detail_rank=value

    #     self.rankpage.switch_rank(rank_type=big_rank)
    #     time.sleep(0.5)
    #     self.rankpage.switch_detail_rank(rank_type=big_rank,detail_type=detail_rank)

    #     if big_rank=="note":
    #         scroll_high=950
    #     else:
    #         scroll_high=600


    #     self.rankpage.scroll(high=scroll_high,duration=1000)

    #     time.sleep(0.5)
    #     self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
    #     self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))

    #     if big_rank!="note":
    #         for i in range(2): 
    #             self.rankpage.get_element(self.rankpage.author_date_choice).click()
    #             time.sleep(0.3)
    #             self.rankpage.get_element(self.rankpage.day_week_month_select).move(0,-40,200)
    #             time.sleep(0.5)
    #             self.rankpage.get_element(self.rankpage.pop_yes_button).click()
    #             if self.rankpage.is_ele_exist(self.rankpage.pop_yes_button):
    #                 self.rankpage.get_element(self.rankpage.pop_yes_button).click()

    #             time.sleep(0.5)
    #             self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_button,inner_text="升级会员"))
    #             self.assertEqual(True,self.rankpage.is_ele_exist(self.rankpage.upgrade_vip_text,inner_text="升级会员可查看更多数据，"))

    #     else:
    #         pass


