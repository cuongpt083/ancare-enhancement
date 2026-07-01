const { chromium, devices } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const screenshotsDir = path.join(__dirname, 'screenshots');
  if (!fs.existsSync(screenshotsDir)) {
    fs.mkdirSync(screenshotsDir, { recursive: true });
  }

  // Setup browser and iPhone 14 Pro Max emulation
  const browser = await chromium.launch({ headless: true });
  const pixelContext = devices['iPhone 14 Pro Max'];
  const context = await browser.newContext({
    ...pixelContext,
    locale: 'vi-VN',
    timezoneId: 'Asia/Ho_Chi_Minh',
  });

  const page = await context.newPage();

  // Helper function for taking screenshots
  const takeScreenshot = async (name) => {
    const imgPath = path.join(screenshotsDir, name);
    await page.screenshot({ path: imgPath });
    console.log(`[Captured] Saved ${name}`);
  };

  try {
    // 1. Welcome screen
    console.log("Navigating to https://app.ancares.vn ...");
    await page.goto('https://app.ancares.vn', { waitUntil: 'networkidle', timeout: 60000 });
    await takeScreenshot('01_welcome.png');

    // 2. Login screen
    console.log("Navigating to login screen...");
    await page.click('button:has-text("Bắt đầu ngay")');
    await page.waitForTimeout(2000);
    await takeScreenshot('02_login.png');

    // Login execution
    console.log("Filling login credentials...");
    await page.locator('input[type="email"]').first().fill('cuongpt083@gmail.com');
    await page.locator('input[type="password"]').first().fill('Abcd@1234');
    console.log("Submitting login...");
    await page.locator('div:text-is("Đăng nhập")').first().click();
    
    console.log("Waiting for Dashboard to load...");
    await page.waitForTimeout(8000);
    await page.waitForLoadState('networkidle').catch(() => {});

    // 3. Dashboard screen
    await takeScreenshot('03_dashboard.png');

    // 4. Action: Click Tanita update on Dashboard
    console.log("Clicking 'KH 02: Cập nhật chỉ số Tanita' on Dashboard...");
    try {
      if (await page.locator('text="KH 02: Cập nhật chỉ số Tanita"').count() > 0) {
        await page.locator('text="KH 02: Cập nhật chỉ số Tanita"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('04_tanita_update.png');
      } else {
        console.log("Tanita update action not found, taking fallback screenshot...");
        await takeScreenshot('04_tanita_update.png');
      }
    } catch (e) {
      console.error("Error clicking Tanita update:", e.message);
      await takeScreenshot('04_tanita_update.png');
    }

    // 5. Team tab
    console.log("Navigating to Team tab directly...");
    await page.goto('https://app.ancares.vn/team', { waitUntil: 'networkidle' }).catch(() => {});
    await page.waitForTimeout(3000);
    await takeScreenshot('05_team.png');

    // 6. Action: Click Invite new customer
    console.log("Clicking 'Mời KH mới' on Team page...");
    try {
      if (await page.locator('text="Mời KH mới"').count() > 0) {
        await page.locator('text="Mời KH mới"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('06_moi_kh_moi.png');
      } else {
        console.log("Mời KH mới button not found");
        await takeScreenshot('06_moi_kh_moi.png');
      }
    } catch (e) {
      console.error("Error clicking 'Mời KH mới':", e.message);
      await takeScreenshot('06_moi_kh_moi.png');
    }

    // 7. Chat tab
    console.log("Navigating to Chat tab directly...");
    await page.goto('https://app.ancares.vn/chat', { waitUntil: 'networkidle' }).catch(() => {});
    await page.waitForTimeout(3000);
    await takeScreenshot('07_chat.png');

    // 8. Action: Click AI Assistant
    console.log("Clicking 'Trợ lý AI' on Chat page...");
    try {
      if (await page.locator('text="Trợ lý AI"').count() > 0) {
        await page.locator('text="Trợ lý AI"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('08_chat_tro_ly_ai.png');
      } else {
        console.log("Trợ lý AI button not found");
        await takeScreenshot('08_chat_tro_ly_ai.png');
      }
    } catch (e) {
      console.error("Error clicking 'Trợ lý AI':", e.message);
      await takeScreenshot('08_chat_tro_ly_ai.png');
    }

    // 9. Action: Click Community chat
    console.log("Navigating to Chat tab again to click Community...");
    await page.goto('https://app.ancares.vn/chat', { waitUntil: 'networkidle' }).catch(() => {});
    await page.waitForTimeout(2000);
    console.log("Clicking 'Cộng đồng' on Chat page...");
    try {
      if (await page.locator('text="Cộng đồng"').count() > 0) {
        await page.locator('text="Cộng đồng"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('09_chat_cong_dong.png');
      } else {
        console.log("Cộng đồng button not found");
        await takeScreenshot('09_chat_cong_dong.png');
      }
    } catch (e) {
      console.error("Error clicking 'Cộng đồng':", e.message);
      await takeScreenshot('09_chat_cong_dong.png');
    }

    // 10. HLV tab
    console.log("Navigating to HLV tab directly...");
    await page.goto('https://app.ancares.vn/consult', { waitUntil: 'networkidle' }).catch(() => {});
    await page.waitForTimeout(3000);
    await takeScreenshot('10_hlv.png');

    // 11. Action: Click customer details
    console.log("Clicking KH 02 details on HLV page...");
    try {
      if (await page.locator('text="KH 02"').count() > 0) {
        await page.locator('text="KH 02"').first().click();
        await page.waitForTimeout(4000);
        await takeScreenshot('11_chi_tiet_khach_hang.png');
      } else {
        console.log("KH 02 button not found");
        await takeScreenshot('11_chi_tiet_khach_hang.png');
      }
    } catch (e) {
      console.error("Error clicking KH 02 details:", e.message);
      await takeScreenshot('11_chi_tiet_khach_hang.png');
    }

    // 12. Profile tab
    console.log("Navigating to Hồ Sơ (Profile) tab directly...");
    await page.goto('https://app.ancares.vn/profile', { waitUntil: 'networkidle' }).catch(() => {});
    await page.waitForTimeout(3000);
    await takeScreenshot('12_profile.png');

    // 13. Action: Click Create package
    console.log("Clicking 'Tạo gói' on Hồ Sơ page...");
    try {
      if (await page.locator('text="Tạo gói"').count() > 0) {
        await page.locator('text="Tạo gói"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('13_tao_goi.png');
      } else {
        console.log("Tạo gói button not found");
        await takeScreenshot('13_tao_goi.png');
      }
    } catch (e) {
      console.error("Error clicking 'Tạo gói':", e.message);
      await takeScreenshot('13_tao_goi.png');
    }

    console.log("All capturing steps completed successfully!");

  } catch (error) {
    console.error("Global capturing error:", error);
  } finally {
    await browser.close();
  }
})();
