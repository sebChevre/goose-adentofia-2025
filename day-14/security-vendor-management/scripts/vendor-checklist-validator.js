#!/usr/bin/env node
// Vendor Setup Checklist Validator
// Ensures all vendor requirements are met before opening

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(prompt) {
  return new Promise((resolve) => {
    rl.question(prompt, (answer) => {
      resolve(answer.toLowerCase().trim());
    });
  });
}

async function validateVendor() {
  console.log('\n🏪 VENDOR SETUP VALIDATION\n');
  
  const vendorName = await question('Vendor/Business Name: ');
  const boothNumber = await question('Booth Number: ');
  
  console.log(`\nValidating setup for: ${vendorName} (Booth ${boothNumber})\n`);
  
  const checks = [];
  let passed = 0;
  let failed = 0;
  let warnings = 0;
  
  // Payment check
  console.log('--- PAYMENT ---');
  const depositPaid = await question('50% deposit received? (y/n): ');
  if (depositPaid === 'y') {
    console.log('✅ Deposit confirmed');
    checks.push({ item: '50% Deposit', status: 'PASS' });
    passed++;
  } else {
    console.log('❌ CRITICAL: No deposit - vendor cannot setup');
    checks.push({ item: '50% Deposit', status: 'FAIL - CRITICAL' });
    failed++;
  }
  
  // Insurance
  console.log('\n--- INSURANCE ---');
  const insuranceCert = await question('Current insurance certificate on file? (y/n): ');
  if (insuranceCert === 'y') {
    console.log('✅ Insurance verified');
    checks.push({ item: 'Insurance Certificate', status: 'PASS' });
    passed++;
  } else {
    console.log('❌ CRITICAL: No insurance - vendor cannot setup');
    checks.push({ item: 'Insurance Certificate', status: 'FAIL - CRITICAL' });
    failed++;
  }
  
  // Food vendor specific
  const isFoodVendor = await question('\n--- FOOD VENDOR? ---\nIs this a food/beverage vendor? (y/n): ');
  if (isFoodVendor === 'y') {
    console.log('\n--- FOOD SAFETY ---');
    const healthPermit = await question('Health permit verified BEFORE setup? (y/n): ');
    if (healthPermit === 'y') {
      console.log('✅ Health permit verified');
      checks.push({ item: 'Health Permit', status: 'PASS' });
      passed++;
    } else {
      console.log('❌ CRITICAL: No health permit - food vendor cannot operate');
      checks.push({ item: 'Health Permit', status: 'FAIL - CRITICAL' });
      failed++;
    }
    
    const fireExtinguisher = await question('Fire extinguisher visible? (y/n): ');
    if (fireExtinguisher === 'y') {
      console.log('✅ Fire safety confirmed');
      checks.push({ item: 'Fire Extinguisher', status: 'PASS' });
      passed++;
    } else {
      console.log('⚠️  WARNING: Fire extinguisher required');
      checks.push({ item: 'Fire Extinguisher', status: 'WARNING' });
      warnings++;
    }
  }
  
  // Electrical
  console.log('\n--- ELECTRICAL ---');
  const electricalNeeds = await question('Electrical requirements confirmed and met? (y/n/na): ');
  if (electricalNeeds === 'y') {
    console.log('✅ Electrical setup verified');
    checks.push({ item: 'Electrical Setup', status: 'PASS' });
    passed++;
  } else if (electricalNeeds === 'na') {
    console.log('➖ No electrical needed');
    checks.push({ item: 'Electrical Setup', status: 'N/A' });
  } else {
    console.log('⚠️  WARNING: Electrical needs not met');
    checks.push({ item: 'Electrical Setup', status: 'WARNING' });
    warnings++;
  }
  
  // Booth spacing
  console.log('\n--- BOOTH SETUP ---');
  const boothSpacing = await question('Booth dimensions comply with contract? (y/n): ');
  if (boothSpacing === 'y') {
    console.log('✅ Booth spacing compliant');
    checks.push({ item: 'Booth Spacing', status: 'PASS' });
    passed++;
  } else {
    console.log('⚠️  WARNING: Booth spacing violation');
    checks.push({ item: 'Booth Spacing', status: 'WARNING' });
    warnings++;
  }
  
  // Summary
  console.log('\n\n' + '='.repeat(50));
  console.log(`VALIDATION SUMMARY: ${vendorName}`);
  console.log('='.repeat(50));
  
  checks.forEach(check => {
    const icon = check.status.includes('PASS') ? '✅' :
                 check.status.includes('FAIL') ? '❌' :
                 check.status.includes('WARNING') ? '⚠️' : '➖';
    console.log(`${icon} ${check.item.padEnd(30)} ${check.status}`);
  });
  
  console.log('\n' + '-'.repeat(50));
  console.log(`Passed: ${passed} | Failed: ${failed} | Warnings: ${warnings}`);
  console.log('-'.repeat(50) + '\n');
  
  // Final verdict
  if (failed > 0) {
    console.log('🚫 VENDOR CANNOT SETUP - Critical requirements not met');
    console.log('   Action: Vendor must leave until requirements satisfied\n');
  } else if (warnings > 0) {
    console.log('⚠️  CONDITIONAL APPROVAL - Warnings must be addressed');
    console.log('   Action: Note warnings, set deadline for compliance\n');
  } else {
    console.log('✅ APPROVED FOR SETUP - All requirements met');
    console.log('   Action: Vendor may proceed with setup\n');
  }
  
  rl.close();
}

validateVendor().catch(err => {
  console.error('Error:', err);
  rl.close();
  process.exit(1);
});
