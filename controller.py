from selenium import webdriver
from ap_ssh import *
import time


tags_fw = "ftp://10.1.1.47/uap/tags/3.4.8/uap_qca956x/bin/latest_firmware-bootrom.bin"


class AccessPoint:

    #Basic Action#

    def __init__(self, mac):
        self.mac = mac
        self.ip = "https://localhost:8443/login"
        self.user = "admin"
        self.pw = "admin"
        self.driver = webdriver.Firefox()
        self.driver.get(self.ip)

    def login(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_id("LoginUsername").clear()
        driver.find_element_by_id("LoginUsername").send_keys(self.user)
        driver.find_element_by_id("LoginPassword").clear()
        driver.find_element_by_id("LoginPassword").send_keys(self.pw)
        driver.find_element_by_id("LoginButton").click()
        time.sleep(1)

    def device_tab(self):
        driver = self.driver
        driver.find_element_by_css_selector("#navDevices > a > span.nav-text").click()

    def mac_address(self, mac):
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='devicesIndex']/div/div[2]/table/tbody/tr[@class ="
                                     " '" + mac + "']/td[2]").click()

    def configuration_tab(self):
        driver = self.driver
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/ul/li[4]/a").click()

    def radio_tab(self):
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='ui-accordion-3-header-1']/div").click()

    def custom_upgrade_tab(self, link):
        driver = self.driver
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[13]/div").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[14]/button").click()
        textfield = driver.find_element_by_name("upgrade-url")
        textfield.send_keys(link)
        driver.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()
        driver.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()

    def custom_upgrade_tab_stress(self, link):
        driver = self.driver
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[13]/div").click()

        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[14]/button").click()
        textfield = driver.find_element_by_name("upgrade-url")
        textfield.send_keys(link)
        driver.find_element_by_xpath("//div[3]/div/button[1]").click()
        driver.find_element_by_xpath("//div[3]/div/button[1]").click()


     ##   driver.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()
     ##   driver.find_element_by_xpath("html/body/div[8]/div[3]/div/button[1]").click()
        print "sleep begin"
        time.sleep(90)
        print "sleep done"
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[13]/div").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/div/div[14]/button").click()
        textfield = driver.find_element_by_name("upgrade-url")
        textfield.send_keys(link)
        driver.find_element_by_xpath("//div[3]/div/button[1]").click()
        driver.find_element_by_xpath("//div[3]/div/button[1]").click()








    def two_g(self, ht):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/span/a/span[2]").click()
        if ht == 20:
                    driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/div/ul/li[1]/a").click()
        else:
                    driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[1]/div[1]/div/div[2]/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/\
                div/div[4]/form/button").click()

    def five_g(self, ht):
        driver = self.driver
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/span/a/span[2]").click()
        if ht == 20:
                    driver.find_element_by_xpath(" /html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[1]").click()
        elif ht == 40:
                    driver.find_element_by_xpath(" /html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[2]").click()
        else:
                    driver.find_element_by_xpath(" /html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/\
                    div[1]/div[4]/div/div[4]/form/fieldset[2]/div[1]/div/div[2]/div/ul/li[3]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div/div[2]/div[4]/div[1]/div[4]/\
                    div/div[4]/form/button").click()


    #Configure AP#

    def configure_2g_channel_width(self, ht):
        self.login()
        self.device_tab()
        self.mac_address(self.mac)
        self.configuration_tab()
        self.radio_tab()
        self.two_g(ht)

    def configure_5g_channel_width(self, ht):
        self.login()
        self.device_tab()
        self.mac_address(self.mac)
        self.configuration_tab()
        self.radio_tab()
        self.five_g(ht)

    def upgrade_ap(self, link):
        self.login()
        self.device_tab()
        self.mac_address(self.mac)
        self.configuration_tab()
        self.custom_upgrade_tab(link)

    def upgrade_ap_stress(self, link):
        self.login()
        self.device_tab()
        self.mac_address(self.mac)
        self.configuration_tab()
        self.custom_upgrade_tab_stress(link)




if __name__ == "__main__":


    ap = AccessPoint('mac-44d9e702010c')
    link = "ftp://10.1.1.47/uap/heads/feature-uapgen2-stable-bsteering/78_2015-10-26_11%3A36%3A36_xi.chen_b930357/uap_qca956x/bin/latest_firmware-bootrom.bin"
    ap.upgrade_ap_stress(link)




