#!/usr/bin/env node
// Emergency Notification Sender (Mock)
// Simulates sending emergency notifications

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(prompt) {
  return new Promise((resolve) => {
    rl.question(prompt, (answer) => {
      resolve(answer);
    });
  });
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function sendEmergencyNotification() {
  console.log('\n📢 EMERGENCY NOTIFICATION SYSTEM\n');
  console.log('⚠️  MOCK MODE - No actual notifications sent\n');
  
  // Emergency type
  console.log('Emergency Type:');
  console.log('1. Weather Delay');
  console.log('2. Event Cancellation');
  console.log('3. Code Yellow (Lost Child)');
  console.log('4. Code Blue (Medical)');
  console.log('5. Code White (Weather Emergency)');
  console.log('6. Code Orange (Security)');
  
  const typeChoice = await question('\nSelect (1-6): ');
  const types = {
    '1': { name: 'Weather Delay', channels: ['email', 'social', 'website', 'sms'] },
    '2': { name: 'Event Cancellation', channels: ['email', 'website', 'social', 'press'] },
    '3': { name: 'Code Yellow', channels: ['radio', 'staff-chat', 'pa-system'] },
    '4': { name: 'Code Blue', channels: ['radio', 'staff-chat', '911'] },
    '5': { name: 'Code White', channels: ['radio', 'pa-system', 'social', 'sms'] },
    '6': { name: 'Code Orange', channels: ['radio', 'staff-chat', 'security-team'] }
  };
  
  const emergency = types[typeChoice] || types['1'];
  
  console.log(`\n📡 Preparing to send: ${emergency.name}`);
  
  const message = await question('\nMessage content (brief): ');
  
  console.log(`\n🚀 Sending to channels: ${emergency.channels.join(', ')}\n`);
  
  // Simulate sending to each channel
  for (const channel of emergency.channels) {
    process.stdout.write(`   Sending to ${channel.padEnd(20)} `);
    await sleep(500);
    console.log('✅');
  }
  
  console.log('\n' + '='.repeat(50));
  console.log('NOTIFICATION SUMMARY');
  console.log('='.repeat(50));
  console.log(`Type: ${emergency.name}`);
  console.log(`Channels: ${emergency.channels.length}`);
  console.log(`Message: "${message}"`);
  console.log(`Timestamp: ${new Date().toISOString()}`);
  console.log('='.repeat(50));
  
  console.log('\n📋 Recommended Follow-up Actions:\n');
  
  if (emergency.name === 'Weather Delay') {
    console.log('   1. Post updates every 30 minutes');
    console.log('   2. Monitor weather conditions');
    console.log('   3. Prepare "all clear" message');
    console.log('   4. Update staff on timeline\n');
  } else if (emergency.name === 'Event Cancellation') {
    console.log('   1. Process refunds within 24 hours');
    console.log('   2. Monitor customer service channels');
    console.log('   3. Send follow-up email with details');
    console.log('   4. Update all online listings\n');
  } else if (emergency.name.startsWith('Code')) {
    console.log('   1. Monitor situation closely');
    console.log('   2. Provide regular updates to team');
    console.log('   3. Document all actions taken');
    console.log('   4. Send "all clear" when resolved\n');
  }
  
  console.log('⚠️  REMINDER: This was a MOCK notification');
  console.log('   In production, this would send real alerts\n');
  
  rl.close();
}

sendEmergencyNotification().catch(err => {
  console.error('Error:', err);
  rl.close();
  process.exit(1);
});
