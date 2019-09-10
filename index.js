const fs = require('fs');
const data = readFile("data/stations-1548092487.json");

let statsPerBike = {};
for (let i = 0; i < data.features.length; i ++) {
    const feature = data.features[i];

    if (statsPerBike[feature.id]) {
        statsPerBike.properties.push(feature.properties);
    } else {
        statsPerBike = {
            ...statsPerBike,
            [feature.id]: {
                id: feature.id,
                coordinates: feature.geometry.coordinates[0],
                name: feature.properties.desig_comercial,
                properties: [feature.properties]
            }
        }
    }
}

function readFile(filepath, cb) {
    const data = fs.readFileSync(filepath, 'utf8');

    return JSON.parse(data);
}
