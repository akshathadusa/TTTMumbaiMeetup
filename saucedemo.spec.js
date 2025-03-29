// @ts-check
import { test, expect } from '@playwright/test';
import {ai} from "@zerostep/playwright"


test('Login Practise Page', async ({ page }) => {

  const aiArgs= {page,test}
 
  await  page.goto('https://www.saucedemo.com/')
  await ai('Enter "standard_user" as Username',aiArgs )
  await ai('Enter "secret_sauce" as Password',aiArgs)
  await ai('Click Login',aiArgs)
  await page.waitForTimeout(8_000)
  await page.evaluate(()=> window.scrollTo(0,document.body.scrollHeight));
  await ai('Click Add to cart associated with "Sauce Labs Bike Light" ',aiArgs)
  await ai('Go to the checkout page ',aiArgs)
  await ai('Click checkout button',aiArgs)
  await ai('Enter Testuser in Firstname input ',aiArgs)
  await ai('Enter Testuser in Lastname input ',aiArgs)
  await ai('Enter 400123 in Zip input ',aiArgs)
  await ai('Click Continue button',aiArgs)
  await ai('Click on Finish button',aiArgs)
  const text=await ai('Confirm that success confirmation text is displayed',aiArgs)
  expect(text).toEqual(true)

});


