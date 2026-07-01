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
        
        // Go back to dashboard by clicking dashboard tab
        await page.locator('a[role="tab"][href="/dashboard"]').click();
        await page.waitForTimeout(2000);
      } else {
        console.log("Tanita update action not found, taking fallback screenshot...");
        await takeScreenshot('04_tanita_update_skipped.png');
      }
    } catch (e) {
      console.error("Error clicking Tanita update:", e.message);
      await takeScreenshot('04_tanita_update_error.png');
      await page.locator('a[role="tab"][href="/dashboard"]').click().catch(() => {});
      await page.waitForTimeout(2000);
    }

    // 5. Team tab
    console.log("Navigating to Team tab...");
    await page.locator('a[role="tab"][href="/team"]').click();
    await page.waitForTimeout(3000);
    await takeScreenshot('05_team.png');

    // 6. Action: Click Invite new customer
    console.log("Clicking 'Mời KH mới' on Team page...");
    try {
      if (await page.locator('text="Mời KH mới"').count() > 0) {
        await page.locator('text="Mời KH mới"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('06_moi_kh_moi.png');

        // Reset to Team tab
        await page.locator('a[role="tab"][href="/team"]').click();
        await page.waitForTimeout(2000);
      } else {
        console.log("Mời KH mới button not found");
        await takeScreenshot('06_moi_kh_moi_skipped.png');
      }
    } catch (e) {
      console.error("Error clicking 'Mời KH mới':", e.message);
      await takeScreenshot('06_moi_kh_moi_error.png');
      await page.locator('a[role="tab"][href="/team"]').click().catch(() => {});
      await page.waitForTimeout(2000);
    }

    // 7. Chat tab
    console.log("Navigating to Chat tab...");
    await page.locator('a[role="tab"][href="/chat"]').click();
    await page.waitForTimeout(3000);
    await takeScreenshot('07_chat.png');

    // 8. Action: Click AI Assistant
    console.log("Clicking 'Trợ lý AI' on Chat page...");
    try {
      if (await page.locator('text="Trợ lý AI"').count() > 0) {
        await page.locator('text="Trợ lý AI"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('08_chat_tro_ly_ai.png');

        // Reset to Chat tab
        await page.locator('a[role="tab"][href="/chat"]').click();
        await page.waitForTimeout(2000);
      } else {
        console.log("Trợ lý AI button not found");
        await takeScreenshot('08_chat_tro_ly_ai_skipped.png');
      }
    } catch (e) {
      console.error("Error clicking 'Trợ lý AI':", e.message);
      await takeScreenshot('08_chat_tro_ly_ai_error.png');
      await page.locator('a[role="tab"][href="/chat"]').click().catch(() => {});
      await page.waitForTimeout(2000);
    }

    // 9. Action: Click Community chat
    console.log("Clicking 'Cộng đồng' on Chat page...");
    try {
      if (await page.locator('text="Cộng đồng"').count() > 0) {
        await page.locator('text="Cộng đồng"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('09_chat_cong_dong.png');

        // Reset to Chat tab
        await page.locator('a[role="tab"][href="/chat"]').click();
        await page.waitForTimeout(2000);
      } else {
        console.log("Cộng đồng button not found");
        await takeScreenshot('09_chat_cong_dong_skipped.png');
      }
    } catch (e) {
      console.error("Error clicking 'Cộng đồng':", e.message);
      await takeScreenshot('09_chat_cong_dong_error.png');
      await page.locator('a[role="tab"][href="/chat"]').click().catch(() => {});
      await page.waitForTimeout(2000);
    }

    // 10. HLV tab
    console.log("Navigating to HLV tab...");
    await page.locator('a[role="tab"][href="/consult"]').click();
    await page.waitForTimeout(3000);
    await takeScreenshot('10_hlv.png');

    // 11. Action: Click customer details
    console.log("Clicking KH 02 details on HLV page...");
    try {
      if (await page.locator('text="KH 02"').count() > 0) {
        await page.locator('text="KH 02"').first().click();
        await page.waitForTimeout(4000); // detail pages might load remote data
        await takeScreenshot('11_chi_tiet_khach_hang.png');

        // Reset to HLV tab
        await page.locator('a[role="tab"][href="/consult"]').click();
        await page.waitForTimeout(2000);
      } else {
        console.log("KH 02 button not found");
        await takeScreenshot('11_chi_tiet_khach_hang_skipped.png');
      }
    } catch (e) {
      console.error("Error clicking KH 02 details:", e.message);
      await takeScreenshot('11_chi_tiet_khach_hang_error.png');
      await page.locator('a[role="tab"][href="/consult"]').click().catch(() => {});
      await page.waitForTimeout(2000);
    }

    // 12. Profile tab
    console.log("Navigating to Hồ Sơ (Profile) tab...");
    await page.locator('a[role="tab"][href="/profile"]').click();
    await page.waitForTimeout(3000);
    await takeScreenshot('12_profile.png');

    // 13. Action: Click Create package
    console.log("Clicking 'Tạo gói' on Hồ Sơ page...");
    try {
      if (await page.locator('text="Tạo gói"').count() > 0) {
        await page.locator('text="Tạo gói"').first().click();
        await page.waitForTimeout(3000);
        await takeScreenshot('13_tao_goi.png');

        // Reset to Profile tab
        await page.locator('a[role="tab"][href="/profile"]').click();
        await page.waitForTimeout(2000);
      } else {
        console.log("Tạo gói button not found");
        await takeScreenshot('13_tao_goi_skipped.png');
      }
    } catch (e) {
      console.error("Error clicking 'Tạo gói':", e.message);
      await takeScreenshot('13_tao_goi_error.png');
      await page.locator('a[role="tab"][href="/profile"]').click().catch(() => {});
      await page.waitForTimeout(2000);
    }

    console.log("All capturing steps completed successfully!");

  } catch (error) {
    console.error("Global capturing error:", error);
  } finally {
    await browser.close();
  }
})();
