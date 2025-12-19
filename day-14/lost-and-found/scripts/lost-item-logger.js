#!/usr/bin/env node
// Lost Item Logger
// Quick logging for found items

const readline = require('readline');
const fs = require('fs');
const path = require('path');

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

async function logLostItem() {
  console.log('\n📦 LOST ITEM LOGGER\n');

  const item = {};
  
  // Basic item info
  item.itemNumber = `LF-${Date.now()}`;
  item.date = new Date().toISOString().split('T')[0];
  item.time = new Date().toTimeString().split(' ')[0];
  
  // Item details
  console.log('What type of item?');
  console.log('1. Phone/Electronics');
  console.log('2. Wallet/Purse');
  console.log('3. Keys');
  console.log('4. Clothing');
  console.log('5. Stuffed Animal/Toy');
  console.log('6. Other');
  
  const typeChoice = await question('\nSelect (1-6): ');
  const types = {
    '1': 'Phone/Electronics',
    '2': 'Wallet/Purse',
    '3': 'Keys',
    '4': 'Clothing',
    '5': 'Stuffed Animal/Toy',
    '6': 'Other'
  };
  item.type = types[typeChoice] || 'Other';
  
  item.description = await question('\nBrief description (color, brand, features): ');
  
  // Location found
  console.log('\nWhere was it found?');
  console.log('1. Ice Rink');
  console.log('2. Food Court');
  console.log('3. Vendor Area');
  console.log('4. Bathroom');
  console.log('5. Entrance/Exit');
  console.log('6. Other');
  
  const locationChoice = await question('\nSelect (1-6): ');
  const locations = {
    '1': 'Ice Rink',
    '2': 'Food Court',
    '3': 'Vendor Area',
    '4': 'Bathroom',
    '5': 'Entrance/Exit',
    '6': 'Other'
  };
  item.location = locations[locationChoice] || 'Other';
  
  item.specificLocation = await question('Specific location details: ');
  item.finderName = await question('\nYour name (finder): ');
  
  // Priority assessment
  const isUrgent = item.type === 'Stuffed Animal/Toy' || 
                   item.type === 'Phone/Electronics' || 
                   item.type === 'Wallet/Purse' ||
                   item.type === 'Keys';
  
  item.priority = isUrgent ? 'HIGH' : 'NORMAL';
  
  // Storage location
  const isHighValue = item.type === 'Phone/Electronics' || 
                      item.type === 'Wallet/Purse' || 
                      item.type === 'Keys';
  
  item.storage = isHighValue ? 'LOCKED CABINET' : 'Open Shelf';

  // Generate log entry
  const logEntry = `
# LOST ITEM LOG ENTRY

**Item Number:** ${item.itemNumber}
**Date Found:** ${item.date}
**Time Found:** ${item.time}
**Priority:** ${item.priority}

---

## Item Details

**Type:** ${item.type}
**Description:** ${item.description}

**Location Found:** ${item.location}
**Specific Location:** ${item.specificLocation}

**Found By:** ${item.finderName}

---

## Storage & Handling

**Storage Location:** ${item.storage}
**Photo Taken:** [ ] Yes [ ] No (REQUIRED)

**Tag Information:**
- Item #: ${item.itemNumber}
- Description: ${item.description}
- Location: ${item.location} - ${item.specificLocation}
- Time: ${item.time}
- Finder: ${item.finderName}

---

## Next Steps

${item.priority === 'HIGH' ? 
  `⚠️  HIGH PRIORITY ITEM
  - [ ] Photo taken immediately
  - [ ] Stored in locked cabinet
  - [ ] Consider announcement if stuffed animal
  - [ ] Monitor for claims closely` :
  `- [ ] Photo taken
  - [ ] Tagged and stored
  - [ ] Added to master log`
}

---

**Status:** Awaiting Claim
**Logged:** ${new Date().toISOString()}
`;

  // Append to daily log
  const filename = `lost-found-log-${item.date}.md`;
  const outputPath = path.join(process.cwd(), filename);
  
  const quickSummary = `[${item.time}] #${item.itemNumber} - ${item.type}: ${item.description} - Found at ${item.location}\n`;
  
  if (fs.existsSync(outputPath)) {
    fs.appendFileSync(outputPath, '\n---\n' + logEntry);
  } else {
    const header = `# Lost & Found Daily Log - ${item.date}\n\n## Quick Summary\n\n`;
    fs.writeFileSync(outputPath, header + quickSummary + '\n---\n' + logEntry);
  }
  
  console.log(`\n✅ Item logged: ${item.itemNumber}`);
  console.log(`📄 Added to: ${filename}`);
  console.log(`\n⚠️  Remember to:`);
  console.log(`   1. Take photo of item`);
  console.log(`   2. Create physical tag`);
  console.log(`   3. Store in ${item.storage}`);
  
  if (item.priority === 'HIGH') {
    console.log(`\n🔥 HIGH PRIORITY - ${item.type}`);
    if (item.type === 'Stuffed Animal/Toy') {
      console.log(`   Consider announcement: "Stuffed animal found at ${item.location}"`);
    }
  }
  
  console.log('');
  
  rl.close();
}

logLostItem().catch(err => {
  console.error('Error logging item:', err);
  rl.close();
  process.exit(1);
});
