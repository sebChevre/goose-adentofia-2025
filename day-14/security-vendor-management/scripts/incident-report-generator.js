#!/usr/bin/env node
// Incident Report Generator
// Usage: node incident-report-generator.js

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

async function generateIncidentReport() {
  console.log('\n🚨 INCIDENT REPORT GENERATOR\n');
  console.log('This will guide you through creating a complete incident report.\n');

  const data = {};

  // Basic Info
  data.date = new Date().toISOString().split('T')[0];
  data.time = new Date().toTimeString().split(' ')[0];
  data.reportedBy = await question('Your name: ');

  // Incident Type
  console.log('\nIncident Type:');
  console.log('1. Medical Emergency (Code Blue)');
  console.log('2. Lost Child (Code Yellow)');
  console.log('3. Weather Emergency (Code White)');
  console.log('4. Suspicious Activity (Code Orange)');
  console.log('5. Vendor Dispute');
  console.log('6. Customer Complaint');
  console.log('7. Other');
  
  const typeChoice = await question('\nSelect type (1-7): ');
  const types = {
    '1': 'Medical Emergency (Code Blue)',
    '2': 'Lost Child (Code Yellow)',
    '3': 'Weather Emergency (Code White)',
    '4': 'Suspicious Activity (Code Orange)',
    '5': 'Vendor Dispute',
    '6': 'Customer Complaint',
    '7': 'Other'
  };
  data.type = types[typeChoice] || 'Other';

  // Severity
  console.log('\nSeverity:');
  console.log('1. Critical (required 911/emergency services)');
  console.log('2. High (required supervisor intervention)');
  console.log('3. Medium (resolved on-site)');
  console.log('4. Low (documented for records)');
  
  const severityChoice = await question('\nSelect severity (1-4): ');
  const severities = {
    '1': 'Critical',
    '2': 'High',
    '3': 'Medium',
    '4': 'Low'
  };
  data.severity = severities[severityChoice] || 'Medium';

  // Location and Details
  data.location = await question('\nLocation of incident: ');
  data.description = await question('Brief description of what happened: ');

  // People involved
  data.personName = await question('\nPrimary person involved (name or N/A): ');
  data.witnesses = await question('Any witnesses? (names or N/A): ');
  
  // Actions taken
  console.log('\nWhat immediate actions were taken?');
  console.log('1. Called 911');
  console.log('2. Activated emergency code');
  console.log('3. First aid administered');
  console.log('4. Area secured');
  console.log('5. Other');
  
  data.actionTaken = await question('\nSelect action (or describe): ');

  // Generate report
  const reportNumber = `IR-${data.date.replace(/-/g, '')}-${Math.floor(Math.random() * 1000).toString().padStart(3, '0')}`;
  
  const report = `
# INCIDENT REPORT

**Report Number:** ${reportNumber}
**Date of Incident:** ${data.date}
**Time of Incident:** ${data.time}
**Reported By:** ${data.reportedBy}
**Date Report Filed:** ${data.date}

---

## Incident Classification

**Type:** ${data.type}
**Severity:** ${data.severity}

---

## Location & Details

**Location:** ${data.location}

**Description:**
${data.description}

---

## People Involved

**Primary Individual:** ${data.personName}
**Witnesses:** ${data.witnesses}

---

## Response & Actions Taken

**Immediate Actions:**
${data.actionTaken}

**Time Resolved:** [Pending]

---

## Follow-Up Required

- [ ] Document completion
- [ ] Supervisor review
- [ ] Insurance notification (if applicable)

---

**Status:** DRAFT - Requires review and signatures

**Generated:** ${new Date().toISOString()}
`;

  // Save to file
  const filename = `incident-report-${reportNumber}.md`;
  const outputPath = path.join(process.cwd(), filename);
  
  fs.writeFileSync(outputPath, report);
  
  console.log(`\n✅ Incident report generated: ${filename}`);
  console.log(`📄 Location: ${outputPath}`);
  console.log('\n⚠️  Remember to:');
  console.log('   1. Complete all sections');
  console.log('   2. Get supervisor review');
  console.log('   3. File with festival records\n');
  
  rl.close();
}

generateIncidentReport().catch(err => {
  console.error('Error generating report:', err);
  rl.close();
  process.exit(1);
});
