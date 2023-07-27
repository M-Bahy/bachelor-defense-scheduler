import { read } from 'xlsx';

const f = await (await fetch("https://sheetjs.com/pres.xlsx")).arrayBuffer();
const wb = read(f);
console.log(wb);