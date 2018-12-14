const fs = require("fs");

const lines = fs
  .readFileSync("input.txt")
  .toString()
  .split("\n");

const claims = lines.map(v => {
  let [_, x, y, xLength, yLength] = v.match(/(\d{1,})/g).map(a => parseInt(a));
  let area = [];
  for (xi = 0; xi < xLength; xi++) {
    for (yi = 0; yi < yLength; yi++) {
      area.push({ x: xi + x, y: yi + y });
    }
  }
  return area;
});

const grid = buildGrid();
var overlaps = 0;

grid.forEach(square => {
  let overlap = claims.filter(claim => {
    return claim.find(c => {
      if (c.x === square.x && c.y === square.y) return true;
    });
  });
  if (overlap.length > 1) overlaps++;
});

console.log(overlaps);

function buildGrid() {
  let grid = [];
  for (x = 0; x < 1000; x++) {
    for (y = 0; y < 1000; y++) {
      grid.push({ x, y });
    }
  }
  return grid;
}
