import * as THREE from './src/Three.js';
import {OrbitControls} from './src/controls/OrbitControls.js';
import * as BufferGeometryUtils from "./libs/BufferGeometryUtils.js";
import {EdgesGeometry} from './src/geometries/EdgesGeometry.js';

const container = document.getElementById('mapScene');

container.style.cursor = 'auto';


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer();
const bodyBackgroundColor = getComputedStyle(document.body).backgroundColor;
renderer.setClearColor(bodyBackgroundColor);
renderer.setSize(window.innerWidth * 0.97, window.innerHeight * 0.7);
container.appendChild(renderer.domElement);

const outlineMaterial = new THREE.LineBasicMaterial({color: 0xffffff, linewidth: 10});

const loja43 = new THREE.BoxGeometry(15.5, 1, 5);
const loja43pt2 = new THREE.BoxGeometry(2, 1, 1);

const loja53 = new THREE.BoxGeometry(2, 1, 5.5);
const wcPequena = new THREE.BoxGeometry(1, 1, 1.5);
const wcPequena2 = new THREE.BoxGeometry(1, 1, 1.25);
const lojaMicro = new THREE.BoxGeometry(1, 1, 1);
const lojaMicro2 = new THREE.BoxGeometry(1.25, 1, 1.2);
const lojaMicro3 = new THREE.BoxGeometry(1.25, 1, 1.4);
const lojaWide = new THREE.BoxGeometry(2, 1, 1);
const lojaPequena = new THREE.BoxGeometry(1, 1, 2);
const lojaMedia = new THREE.BoxGeometry(1.5, 1, 2);
const loja27Geo = new THREE.BoxGeometry(6, 1, 2);
const lojaMedia2 = new THREE.BoxGeometry(1.5, 1, 1.5);
const lojaGrande = new THREE.BoxGeometry(2, 1, 2);
const longMesh = new THREE.BoxGeometry(5, 1, 4);
const smallMesh = new THREE.BoxGeometry(1, 1, 1);

const materialDefault = new THREE.MeshBasicMaterial({color: 0xa2a4a6});
const materialHovered = new THREE.MeshBasicMaterial({color: 0xd9d9d9});
const materialWc = new THREE.MeshBasicMaterial({color: 0x4b4beb});
const planeMaterial = new THREE.MeshBasicMaterial({color: 0xededf0});

loja43pt2.translate(-5.25, 0, 3)
const loja43Total = BufferGeometryUtils.mergeGeometries([loja43, loja43pt2])

longMesh.translate(-0.5, 0, -3)
const loja27 = BufferGeometryUtils.mergeGeometries([loja27Geo, longMesh]);

smallMesh.translate(1.25, 0, -0.25)
const loja61 = BufferGeometryUtils.mergeGeometries([smallMesh, lojaMedia2]);


let cubeYPos = -2;

const storeData = [
    //Stores
    {position: {x: -2, y: cubeYPos, z: -10}, size: lojaMicro, modalId: 'id1', imagePath: "media/storeLogo/id1"},
    {position: {x: 4.25, y: cubeYPos, z: -7.25}, size: lojaWide, modalId: 'id2', imagePath: "media/storeLogo/id2"},
    {position: {x: 6.25, y: cubeYPos, z: -7.25}, size: lojaWide, modalId: 'id3', imagePath: "media/storeLogo/id3"},
    {position: {x: 8.25, y: cubeYPos, z: -7.25}, size: lojaWide, modalId: 'id4', imagePath: "media/storeLogo/id4"},
    {position: {x: 10.25, y: cubeYPos, z: -7.25}, size: lojaWide, modalId: 'id5', imagePath: "media/storeLogo/id5"},
    {position: {x: 12.25, y: cubeYPos, z: -7.25}, size: lojaWide, modalId: 'id6', imagePath: "media/storeLogo/id6"},
    {position: {x: -1.5, y: cubeYPos, z: -5}, size: lojaGrande, modalId: 'id7', imagePath: "media/storeLogo/id7"},
    {position: {x: 0.25, y: cubeYPos, z: -5}, size: lojaMedia, modalId: 'id8', imagePath: "media/storeLogo/id8"},
    {position: {x: 2.75, y: cubeYPos, z: -5}, size: lojaMedia, modalId: 'id9', imagePath: "media/storeLogo/id9"},
    {position: {x: 4, y: cubeYPos, z: -5}, size: lojaPequena, modalId: 'id10', imagePath: "media/storeLogo/id10"},
    {position: {x: 6.25, y: cubeYPos, z: -5}, size: lojaGrande, modalId: 'id11', imagePath: "media/storeLogo/id11"},
    {
        position: {x: 7.75, y: cubeYPos, z: -5},
        size: lojaPequena,
        modalId: 'id12',
        imagePath: "media/storeLogo/id12"
    },
    {
        position: {x: 8.75, y: cubeYPos, z: -5},
        size: lojaPequena,
        modalId: 'id13',
        imagePath: "media/storeLogo/id13"
    },
    {
        position: {x: 10.75, y: cubeYPos, z: -5},
        size: lojaPequena,
        modalId: 'id14',
        imagePath: "media/storeLogo/id14"
    },
    {
        position: {x: 12.25, y: cubeYPos, z: -5},
        size: lojaGrande,
        modalId: 'id15',
        imagePath: "media/storeLogo/id15"
    },
    {
        position: {x: 12.25, y: cubeYPos, z: -3},
        size: lojaGrande,
        modalId: 'id16',
        imagePath: "media/storeLogo/id16"
    },
    {
        position: {x: 10.25, y: cubeYPos, z: -3},
        size: lojaGrande,
        modalId: 'id17',
        imagePath: "media/storeLogo/id17"
    },
    {
        position: {x: 8.75, y: cubeYPos, z: -3},
        size: lojaPequena,
        modalId: 'id18',
        imagePath: "media/storeLogo/id18"
    },
    {
        position: {x: 7.75, y: cubeYPos, z: -3},
        size: lojaPequena,
        modalId: 'id19',
        imagePath: "media/storeLogo/id19"
    },
    {position: {x: 6.25, y: cubeYPos, z: -3}, size: lojaGrande, modalId: 'id20', imagePath: "media/storeLogo/id20"},
    {position: {x: 4, y: cubeYPos, z: -3}, size: lojaPequena, modalId: 'id21', imagePath: "media/storeLogo/id21"},
    {position: {x: 3, y: cubeYPos, z: -3}, size: lojaPequena, modalId: 'id22', imagePath: "media/storeLogo/id22"},
    {position: {x: 2, y: cubeYPos, z: -3}, size: lojaPequena, modalId: 'id23', imagePath: "media/storeLogo/id23"},
    {position: {x: 1, y: cubeYPos, z: -3}, size: lojaPequena, modalId: 'id24', imagePath: "media/storeLogo/id24"},
    {position: {x: 0, y: cubeYPos, z: -3}, size: lojaPequena, modalId: 'id25', imagePath: "media/storeLogo/id25"},
    {position: {x: -1.5, y: cubeYPos, z: -3}, size: lojaGrande, modalId: 'id26', imagePath: "media/storeLogo/id26"},
    {position: {x: -5.5, y: cubeYPos, z: 0}, size: loja27, modalId: 'id27', imagePath: "media/storeLogo/id27"},
    {position: {x: -1.5, y: cubeYPos, z: 0}, size: lojaGrande, modalId: 'id28', imagePath: "media/storeLogo/id28"},
    {position: {x: 0, y: cubeYPos, z: 0}, size: lojaPequena, modalId: 'id29', imagePath: "media/storeLogo/id29"},
    {position: {x: 1, y: cubeYPos, z: 0}, size: lojaPequena, modalId: 'id30', imagePath: "media/storeLogo/id30"},
    {position: {x: 2, y: cubeYPos, z: 0}, size: lojaPequena, modalId: 'id31', imagePath: "media/storeLogo/id31"},
    {position: {x: 3.25, y: cubeYPos, z: 0}, size: lojaMedia, modalId: 'id32', imagePath: "media/storeLogo/id32"},
    {position: {x: 5.5, y: cubeYPos, z: 0}, size: lojaGrande, modalId: 'id33', imagePath: "media/storeLogo/id33"},
    {position: {x: 7, y: cubeYPos, z: 0}, size: lojaPequena, modalId: 'id34', imagePath: "media/storeLogo/id34"},
    {position: {x: 8, y: cubeYPos, z: 0}, size: lojaPequena, modalId: 'id35', imagePath: "media/storeLogo/id35"},
    {position: {x: 9, y: cubeYPos, z: 0}, size: lojaPequena, modalId: 'id36', imagePath: "media/storeLogo/id36"},
    {position: {x: 10, y: cubeYPos, z: 0}, size: lojaPequena, modalId: 'id37', imagePath: "media/storeLogo/id37"},
    {position: {x: 11.25, y: cubeYPos, z: 0}, size: lojaMedia, modalId: 'id38', imagePath: "media/storeLogo/id38"},
    {
        position: {x: 13.25, y: cubeYPos, z: 0},
        size: lojaPequena,
        modalId: 'id39',
        imagePath: "media/storeLogo/id39"
    },
    {
        position: {x: 15, y: cubeYPos, z: -2.65},
        size: lojaMicro3,
        modalId: 'id40',
        imagePath: "media/storeLogo/id40"
    },
    {
        position: {x: 15, y: cubeYPos, z: -3.95},
        size: lojaMicro2,
        modalId: 'id41',
        imagePath: "media/storeLogo/id41"
    },
    {
        position: {x: 15, y: cubeYPos, z: -5.25},
        size: lojaMicro3,
        modalId: 'id42',
        imagePath: "media/storeLogo/id42"
    },
    {
        position: {x: 7.5, y: cubeYPos, z: -10.25},
        size: loja43Total,
        modalId: 'id43',
        imagePath: "media/storeLogo/id43"
    },
    {
        position: {x: 13.75, y: cubeYPos, z: -7.25},
        size: lojaMicro,
        modalId: 'id44',
        imagePath: "media/storeLogo/id44"
    },
    {
        position: {x: 16.25, y: cubeYPos, z: -5.25},
        size: lojaMicro3,
        modalId: 'id45',
        imagePath: "media/storeLogo/id45"
    },
    {
        position: {x: 16.25, y: cubeYPos, z: -3.95},
        size: lojaMicro2,
        modalId: 'id46',
        imagePath: "media/storeLogo/id46"
    },
    {
        position: {x: 16.25, y: cubeYPos, z: -2.65},
        size: lojaMicro3,
        modalId: 'id47',
        imagePath: "media/storeLogo/id47"
    },
    {
        position: {x: 16.25, y: cubeYPos, z: -0.75},
        size: lojaMicro,
        modalId: 'id48',
        imagePath: "media/storeLogo/id48"
    },
    {
        position: {x: 17.25, y: cubeYPos, z: -0.75},
        size: lojaMicro,
        modalId: 'id49',
        imagePath: "media/storeLogo/id49"
    },
    {
        position: {x: 18.75, y: cubeYPos, z: -1.25},
        size: lojaGrande,
        modalId: 'id50',
        imagePath: "media/storeLogo/id50"
    },
    {
        position: {x: 18.75, y: cubeYPos, z: -3.25},
        size: lojaGrande,
        modalId: 'id51',
        imagePath: "media/storeLogo/id51"
    },
    {
        position: {x: 18.75, y: cubeYPos, z: -5.25},
        size: lojaGrande,
        modalId: 'id52',
        imagePath: "media/storeLogo/id52"
    },
    {
        position: {x: 18.75, y: cubeYPos, z: -10},
        size: loja53, modalId: 'id53',
        imagePath: "media/storeLogo/id53"
    },
    {
        position: {x: -3, y: cubeYPos, z: -7.25},
        size: lojaMicro, modalId: 'id56',
        imagePath: "media/storeLogo/id56"
    },
    {
        position: {x: 14.75, y: cubeYPos, z: -7.25},
        size: lojaMicro,
        modalId: 'id57',
        imagePath: "media/storeLogo/id57"
    },
    {
        position: {x: 16, y: cubeYPos, z: -7.5},
        size: lojaMedia2, modalId: 'id58',
        imagePath: "media/storeLogo/id58"
    },
    {
        position: {x: 16, y: cubeYPos, z: -9},
        size: lojaMedia2, modalId: 'id59',
        imagePath: "media/storeLogo/id59"
    },
    {
        position: {x: 16, y: cubeYPos, z: -10.5},
        size: lojaMedia2,
        modalId: 'id60',
        imagePath: "media/storeLogo/id60"
    },
    {
        position: {x: 16, y: cubeYPos, z: -12},
        size: loja61, modalId: 'id61',
        imagePath: "media/storeLogo/id61"
    },
];

const cubes = [];

let edgesGeometry;
let outline;

const wc1 = new THREE.Mesh(wcPequena2, materialWc);
wc1.position.set(-4, cubeYPos, -5.625);
edgesGeometry = new EdgesGeometry(wc1.geometry);
outline = new THREE.LineSegments(edgesGeometry, outlineMaterial);
outline.position.copy(wc1.position);
outline.scale.copy(wc1.scale);
outline.rotation.copy(wc1.rotation);
outline.scale.multiplyScalar(1.005);

scene.add(outline);
scene.add(wc1);


const wc2 = new THREE.Mesh(wcPequena, materialWc);
wc2.position.set(-4, cubeYPos, -7);
edgesGeometry = new EdgesGeometry(wc2.geometry);
outline = new THREE.LineSegments(edgesGeometry, outlineMaterial);
outline.position.copy(wc2.position);
outline.scale.copy(wc2.scale);
outline.rotation.copy(wc2.rotation);
outline.scale.multiplyScalar(1.005);

scene.add(outline);
scene.add(wc2);


const wc3 = new THREE.Mesh(lojaWide, materialWc);
wc3.position.set(14.75, cubeYPos, 0.5);
edgesGeometry = new EdgesGeometry(wc3.geometry);
outline = new THREE.LineSegments(edgesGeometry, outlineMaterial);
outline.position.copy(wc3.position);
outline.scale.copy(wc3.scale);
outline.rotation.copy(wc3.rotation);
outline.scale.multiplyScalar(1.005);

scene.add(outline);
scene.add(wc3);


const wc4 = new THREE.Mesh(wcPequena2, materialWc);
wc4.position.set(15.25, cubeYPos, -0.63);
edgesGeometry = new EdgesGeometry(wc4.geometry);
outline = new THREE.LineSegments(edgesGeometry, outlineMaterial);
outline.position.copy(wc4.position);
outline.scale.copy(wc4.scale);
outline.rotation.copy(wc4.rotation);
outline.scale.multiplyScalar(1.005);

scene.add(outline);
scene.add(wc4);

// PLANES
const planeGeo = new THREE.BoxGeometry(20, 0, 8);
const plane = new THREE.Mesh(planeGeo, planeMaterial);
plane.position.set(5.5, -2.5, -3);
scene.add(plane);
const planeGeo2 = new THREE.BoxGeometry(4.5, 0, 11);
const plane2 = new THREE.Mesh(planeGeo2, planeMaterial);
plane2.position.set(17.5, -2.5, -6.5);
scene.add(plane2);
const planeGeo3 = new THREE.BoxGeometry(4.5, 0, 7);
const plane3 = new THREE.Mesh(planeGeo3, planeMaterial);
plane3.position.set(-0.25, -2.5, -9.25);
scene.add(plane3);


// WALL
const wallGeo = new THREE.BoxGeometry(0, 1, 5);
const wall = new THREE.Mesh(wallGeo, materialDefault);
wall.position.set(-2.5, cubeYPos, -10.25);
scene.add(wall);

const labelsContainer = document.createElement('div');
labelsContainer.classList.add('labels-container');
document.body.appendChild(labelsContainer);


function addLabel(mesh, text) {
    const spriteMaterial = new THREE.SpriteMaterial({color: 0xffffff});
    const sprite = new THREE.Sprite(spriteMaterial);
    sprite.position.set(0, 0.58, 0); // Adjust the position of the label relative to the mesh
    sprite.scale.set(6, 2.5, 1); // Adjust the scale of the label sprite

    const labelContainer = new THREE.Object3D();
    labelContainer.add(sprite);

    mesh.updateMatrixWorld(); // Make sure the mesh's matrixWorld is up to date
    const labelPosition = new THREE.Vector3();
    labelPosition.setFromMatrixPosition(mesh.matrixWorld);
    labelContainer.position.copy(labelPosition);

    scene.add(labelContainer);

    // Set the label text using a canvas texture
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    context.font = 'Bold 20px Arial';
    context.fillStyle = 'white';
    context.textAlign = 'center';
    context.fillText(text.substring(2), canvas.width / 2, canvas.height / 2);

    sprite.material.map = new THREE.CanvasTexture(canvas);
}

async function fileExists(url) {
    try {
        const response = await fetch(url, {method: 'HEAD'});

        return response.status === 200;
    } catch (error) {
        // An error occurred during the request
        return false;
    }
}

async function findImageURL(imagePath) {
    const supportedExtensions = ["jpg", "png"]; // Add other supported extensions if needed

    // Try each extension until a file is found
    for (const extension of supportedExtensions) {
        const imageURL = `${imagePath}.${extension}`;
        if (await fileExists(imageURL)) {
            return imageURL;
        }
    }
    console.log("NAO ENCONTROU");
    // No matching file found
    return null;
}

const storeLogos = {};

const loadStoreLogos = async () => {
    for (const store of storeData) {
        const imageURL = await findImageURL(store.imagePath);
        if (imageURL) {
            // Image found, load it as a texture and add it to storeLogos
            const imageTexture = new THREE.TextureLoader().load(imageURL);
            storeLogos[store.modalId] = imageTexture;
            console.log(`Found image: ${imageURL}`);
        } else {
            // Image not found
            console.log(`Image not found for ${store.modalId}`);
        }
    }
};

await loadStoreLogos();

for (const storeInfo of storeData) {
    let storeMesh = new THREE.Mesh(storeInfo.size, materialDefault);
    const storeNumber = storeInfo.modalId.replace('id', '');

    const edgesGeometry = new THREE.EdgesGeometry(storeMesh.geometry);
    const outline = new THREE.LineSegments(edgesGeometry, outlineMaterial);

    storeMesh.position.set(storeInfo.position.x, storeInfo.position.y, storeInfo.position.z);
    storeMesh.userData.modalId = storeInfo.modalId;

    outline.position.copy(storeMesh.position);
    outline.scale.copy(storeMesh.scale);
    outline.rotation.copy(storeMesh.rotation);
    outline.scale.multiplyScalar(1.005);

    if (storeInfo.imagePath && storeLogos[storeInfo.modalId]) {
        const imageTexture = storeLogos[storeInfo.modalId];
        const aspectRatio = imageTexture.image.width / imageTexture.image.height;
        let imageSize = 1;
        let maxImageHeight = 8;
        if (storeNumber === "43") {
            imageSize = 4;
        } else if (storeNumber === "27") {
            imageSize = 2;
        } else {
            imageSize = Math.min(storeInfo.size.parameters.width * 0.9, 4); // Maximum width of 4
            maxImageHeight = storeInfo.size.parameters.depth; // Maximum height equal to store depth
        }

        // Adjust the image size based on the maximum height constraint
        const adjustedImageSize = Math.min(imageSize, maxImageHeight / aspectRatio);

        const imageMaterial = new THREE.MeshBasicMaterial({map: imageTexture});
        const imageGeometry = new THREE.PlaneGeometry(imageSize, imageSize / aspectRatio);
        const imageMesh = new THREE.Mesh(imageGeometry, imageMaterial);

        imageMesh.position.copy(storeMesh.position);
        imageMesh.position.y += 0.55; // Adjust the height as needed
        imageMesh.rotation.x = Math.PI / -2; // Rotate by 45 degrees

        scene.add(imageMesh);
    }

    scene.add(outline);
    scene.add(storeMesh);
    cubes.push(storeMesh);

    // Add label for the mesh
    addLabel(storeMesh, storeInfo.modalId);
}

const controls = new OrbitControls(camera, renderer.domElement);
controls.target.set(6, 0, -6)
controls.minPolarAngle = Math.PI / 10;
controls.maxPolarAngle = Math.PI / 2;
controls.minDistance = 4;
controls.maxDistance = 45;
controls.enableDamping = true;


camera.position.set(6, 7, 15);

const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();


//container.addEventListener('mousemove', onMouseMove, false);
container.addEventListener('mouseout', onMouseOut, false);
container.addEventListener('click', onMouseClick, false);
window.addEventListener('resize', onWindowResize, false);


function onMouseMove(event) {
    event.preventDefault();
    let cubeHovered = false;

    const containerRect = container.getBoundingClientRect();
    const mouseX = event.clientX - containerRect.left;
    const mouseY = event.clientY - containerRect.top;

    // Store adjusted mouse coordinates in local storage
    localStorage.setItem('mouseX', mouseX);
    localStorage.setItem('mouseY', mouseY);

    mouse.x = (mouseX / container.clientWidth) * 2 - 1;
    mouse.y = -(mouseY / container.clientHeight) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);

    for (const cube of cubes) {
        cube.material = materialDefault;
    }

    for (const intersect of raycaster.intersectObjects(scene.children, true)) {
        const hoveredCube = cubes.find((cube) => cube === intersect.object);
        if (hoveredCube) {
            hoveredCube.material = materialHovered;
            container.style.cursor = 'pointer';
            cubeHovered = true;
            break;
        }
    }

    if (!cubeHovered) {
        container.style.cursor = 'auto';
    }
}

// Retrieve mouse coordinates from local storage on page load
window.addEventListener('load', function() {
    const storedMouseX = localStorage.getItem('mouseX');
    const storedMouseY = localStorage.getItem('mouseY');

    if (storedMouseX && storedMouseY) {
        // Call onMouseMove with the retrieved mouse coordinates
        onMouseMove({ clientX: storedMouseX, clientY: storedMouseY });
    }
});

// Attach the event listener to the window
window.addEventListener('mousemove', onMouseMove);

function onMouseOut() {
    for (const cube of cubes) {
        cube.material = materialDefault;
        container.style.cursor = 'auto';
    }
}

function onMouseClick(event) {
    event.preventDefault();

    raycaster.setFromCamera(mouse, camera);

    for (const intersect of raycaster.intersectObjects(scene.children, true)) {
        const clickedCube = cubes.find((cube) => cube === intersect.object);
        if (clickedCube) {
            const modalId = clickedCube.userData.modalId;
            $(`#${modalId}`).modal('show');
            break;
        }
    }
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize(window.innerWidth * 0.97, window.innerHeight * 0.7);
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();

    renderer.render(scene, camera);
}

animate();