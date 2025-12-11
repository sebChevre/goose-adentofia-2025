import { readFileSync } from 'fs';

interface Vendor {
  name: string;
  location: string;
  cuisine?: string;
}

interface VendorData {
  vendors: Vendor[];
}

const data: VendorData = JSON.parse(
  readFileSync('./vendors.json', 'utf-8')
);

console.log('Vendors\n');

data.vendors.forEach((vendor) => {
  console.log(`Name: ${vendor.name}`);
  console.log(`Location: ${vendor.location}`);
  if (vendor.cuisine) {
    console.log(`Cuisine: ${vendor.cuisine}`);
  }
  console.log('');
});
