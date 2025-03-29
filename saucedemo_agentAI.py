import asyncio
import os

from browser_use.agent.service import Agent
from browser_use.agent.views import ActionResult
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from playwright.sync_api import BrowserContext
from pydantic import BaseModel
from pydantic.v1 import SecretStr


class CheckoutResult(BaseModel):
    login_status: str
    cart_status: str
    checkout_status: str
    total_update_status: str
    delivery_location_status: str
    message_content: str

controller=Controller(output_model=CheckoutResult)


@controller.action('Get Attribute and url of the page')
async def get_attr_url(browser : BrowserContext):
    page =await browser.get_current_page()
    current_url=page.url
    attr= await page.get_by_text("Products").get_attribute('class')
    page(current_url)
    return ActionResult(extracted_content= 'current url is {current_url} and attribute is {attr}')


async def siteValidation():
    os.environ["GOOGLE_API_KEY"] = "Add your key"

    task=(
        'Important : I am UI Automation tester validating the tasks'
        'open base website "https://www.saucedemo.com/"'
        'Login with username and password. login Details available in the same page'
        'Get Attribute and url of the page'
        'After login, select first product and add to cart'
        'Then checkout and store the value you see in screen'
        'Continue Shopping select second product and add to card'
        'Go to cart and check if value update accordingly'
        'checkout and enter Firstname,Lastname,Postal code'
        'Continue and Finish'
        'verify thankyou message is displayed'
    )


    #api1_key = os.environ["GOOGLE_API_KEY"]
   # llm = ChatOpenAI(model ='gpt-4o-mini')

    #ChatGoogleGenerativeAI ---connect to google apis
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')

    agent= Agent(task = task,
                 llm=llm,
                 controller=controller,
                 use_vision=True)
    history= await agent.run()
    history.save_to_file('agent_results.json')
    test_result = history.final_result()
    print(test_result)

   # validated_result = CheckoutResult.model_validate_json(test_result)

    assert test_result.message_content == ('Thank you for your order! '
                                                'Your order has been dispatched, and will arrive just as fast as the pony can get there!')


asyncio.run(siteValidation())   # trigger point