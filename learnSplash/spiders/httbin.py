import scrapy
from scrapy_splash import SplashRequest

lua = """
function main(splash)
     splash:on_request(function(request)
        request:set_proxy{
            host = "119.114.100.159",
            port = 22992,
            username = '',
            password = '',
        }
     end)
    # assert(splash:wait(args.wait))
    -- 设置请求头
    splash:set_user_agent("Mozilla/5.0")
    return splash:html()
end
"""


class HttbinSpider(scrapy.Spider):
    name = 'httbin'
    # allowed_domains = ['httbin.org/get']
    start_urls = ['https://httpbin.org/get']

    def start_requests(self):
        print(self.start_urls[0])
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3'
        }
        # yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=header)
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            # endpoint='execute',
            args={
                "wait": 3,
                # 'lua_source': lua,
                # "proxy": 'http://119.114.100.159:22992'
            }

        )

    def parse(self, response, **kwargs):
        print(response)
        print(response.text)
