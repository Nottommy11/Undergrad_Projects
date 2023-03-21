const floorTexture = "../ShowRoom/textures/garageFloor.jpg";
const wallTexture = "../ShowRoom/textures/garageWall.jpg";

const f35OBJ = "../ShowRoom/models/aircraft_x-35_obj/x-35_obj/x-35_obj.obj";
const f35MTL = "../ShowRoom/models/aircraft_x-35_obj/x-35_obj/x-35_obj.mtl";
const f35Texture =
  "../ShowRoom/models/aircraft_x-35_obj/x-35_obj/diffuse_map.jpg";

const garageTableGLTF = "../ShowRoom/models/garage_table/scene.gltf";

const aim120GLTF = "../ShowRoom/models/aim120_amraam/scene.gltf";

const toolBoxGLTF = "../ShowRoom/models/toolbox/scene.gltf";

const spotLightGLTF = "../ShowRoom/models/spotlight/scene.gltf";

const floodLightGLTF = "../ShowRoom/models/flood_light/scene.gltf";

let scene,
  camera,
  renderer,
  clock,
  params,
  lights,
  f35,
  garageTable,
  aim120,
  toolBox,
  cylinder,
  mySpotlight,
  floodLight;

let lightTheta = 0;
let cylinderTheta = 0;

init();

function init() {
  clock = new THREE.Clock();

  scene = new THREE.Scene();
  const envMap = new THREE.CubeTextureLoader()
    .setPath("./textures/CubeMap/")
    .load([
      "show.jpg",
      "show.jpg",
      "sky.jpg",
      "grass.jpg",
      "show.jpg",
      "show.jpg",
    ]);

  scene.background = envMap;

  camera = new THREE.PerspectiveCamera(
    60,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  camera.position.set(0, 6, 15); //wide position
  camera.lookAt(0, 0, 0);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  document.body.appendChild(renderer.domElement);

  const controls = new THREE.OrbitControls(camera, renderer.domElement);

  // CREATE ROOM
  const floorMat = new THREE.MeshStandardMaterial();
  floorMat.map = new THREE.TextureLoader().load(floorTexture);
  floorMat.map.wrapS = THREE.RepeatWrapping;
  floorMat.map.wrapT = THREE.RepeatWrapping;
  floorMat.map.repeat.set(1, 1);
  floorMat.roughness = 0.5;
  floorMat.metalness = 0.5;
  floorMat.envMap = envMap;

  const wallMat = new THREE.MeshStandardMaterial();
  wallMat.map = new THREE.TextureLoader().load(wallTexture);
  wallMat.map.wrapS = THREE.RepeatWrapping;
  wallMat.map.wrapT = THREE.RepeatWrapping;
  wallMat.map.repeat.set(1, 1);
  wallMat.roughness = 0.5;
  wallMat.metalness = 0.5;
  wallMat.envMap = envMap;

  const floorAndCeilSize = 35;
  const floorAndCeilingGeo = new THREE.PlaneGeometry(
    floorAndCeilSize,
    floorAndCeilSize
  );

  const wallsSize = 15;
  const wallsGeo = new THREE.PlaneGeometry(floorAndCeilSize, wallsSize);

  const floor = new THREE.Mesh(floorAndCeilingGeo, floorMat);
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = 0;
  floor.receiveShadow = true;
  scene.add(floor);

  const geometry = new THREE.CylinderGeometry(5, 5, 0.5, 32);
  const material = new THREE.MeshStandardMaterial();
  cylinder = new THREE.Mesh(geometry, material);
  cylinder.receiveShadow = true;
  cylinder.position.y = 0;
  scene.add(cylinder);

  const backWall = new THREE.Mesh(wallsGeo, wallMat);
  backWall.position.set(0, wallsSize / 2, -floorAndCeilSize / 2);
  backWall.receiveShadow = true;
  scene.add(backWall);

  const frontWall = new THREE.Mesh(wallsGeo, wallMat);
  frontWall.position.set(0, wallsSize / 2, floorAndCeilSize / 2);
  frontWall.rotation.y = Math.PI;
  frontWall.receiveShadow = true;
  scene.add(frontWall);

  const leftWall = new THREE.Mesh(wallsGeo, wallMat);
  leftWall.rotation.y = Math.PI / 2;
  leftWall.position.set(-floorAndCeilSize / 2, wallsSize / 2, 0);
  leftWall.receiveShadow = true;
  scene.add(leftWall);

  const rightWall = new THREE.Mesh(wallsGeo, wallMat);
  rightWall.rotation.y = Math.PI / -2;
  rightWall.position.set(floorAndCeilSize / 2, wallsSize / 2, 0);
  rightWall.receiveShadow = true;
  scene.add(rightWall);

  const ceiling = new THREE.Mesh(floorAndCeilingGeo, wallMat);
  ceiling.rotation.x = Math.PI / 2;
  ceiling.position.y = wallsSize;
  ceiling.receiveShadow = true;
  scene.add(ceiling);
  // END ROOM

  /* 
  const loader = new THREE.OBJLoader();

  // load a resource
  loader.load(
    // resource URL
    f35OBJ,
    // called when resource is loaded
    function (object) {
      scene.add(object);
    },
    // called when loading is in progresses
    function (xhr) {
      console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
    },
    // called when loading has errors
    function (error) {
      console.log("An error happened");
    }
  );
 */

  // LOAD THE F35
  new THREE.MTLLoader().load(f35MTL, function (materials) {
    materials.preload();
    new THREE.OBJLoader()
      .setMaterials(materials)
      .load(f35OBJ, function (object) {
        object.position.y = 0.35;
        object.scale.set(0.1, 0.1, 0.1);
        var texture = new THREE.TextureLoader().load(f35Texture);
        object.traverse(function (child) {
          // aka setTexture
          if (child instanceof THREE.Mesh) {
            child.material.map = texture;
          }
        });
        object.receiveShadow = true;
        object.castShadow = true;
        f35 = object;
        scene.add(object);
      });
  });

  // LOAD THE GARAGE TABLE
  const garageTableLoader = new THREE.GLTFLoader();
  garageTableLoader.load(garageTableGLTF, function (object) {
    object.scene.traverse(function (child) {
      if (child.isMesh) {
        child.castShadow = true;
        child.receiveShadow = true;
      }
    });
    scene.add(object.scene.children[1]);
    garageTable = new THREE.Object3D();
    garageTable.position.set(-6, 0.4, 8);
    garageTable.rotation.y = Math.PI / 3.2;
    scene.add(garageTable);
    garageTable.add(object.scene.children[0]);
  });

  // LOAD THE AIM 120
  const aim120Loader = new THREE.GLTFLoader();
  aim120Loader.load(aim120GLTF, function (object) {
    object.scene.traverse(function (child) {
      if (child.isMesh) {
        child.castShadow = true;
        child.receiveShadow = true;
      }
    });
    scene.add(object.scene.children[1]);
    aim120 = new THREE.Object3D();
    aim120.position.set(-6, 1.2, 8);
    aim120.rotation.y = Math.PI / 3.2;
    scene.add(aim120);
    aim120.add(object.scene.children[0]);
  });

  // LOAD THE TOOLBOX
  const toolBoxLoader = new THREE.GLTFLoader();
  toolBoxLoader.load(toolBoxGLTF, function (object) {
    object.scene.traverse(function (child) {
      if (child.isMesh) {
        child.castShadow = true;
        child.receiveShadow = true;
      }
    });
    scene.add(object.scene.children[1]);
    toolBox = new THREE.Object3D();
    toolBox.position.set(6, 0, 8);
    toolBox.rotation.y = Math.PI / -1.2;
    scene.add(toolBox);
    toolBox.add(object.scene.children[0]);
  });

  // LOAD THE SPOTLIGHT
  const spotlightLoader = new THREE.GLTFLoader();
  spotlightLoader.load(spotLightGLTF, function (object) {
    object.scene.traverse(function (child) {
      if (child.isMesh) {
        child.castShadow = true;
        child.receiveShadow = true;
      }
    });
    scene.add(object.scene.children[1]);
    mySpotlight = new THREE.Object3D();
    mySpotlight.position.set(0, 0.5, 5);
    mySpotlight.scale.set(0.5, 0.5, 0.5);
    mySpotlight.rotation.y = Math.PI;
    scene.add(mySpotlight);
    mySpotlight.add(object.scene.children[0]);
  });

  // LOAD THE FLOODLIGHT
  const floodLightLoader = new THREE.GLTFLoader();
  floodLightLoader.load(floodLightGLTF, function (object) {
    object.scene.traverse(function (child) {
      if (child.isMesh) {
        child.castShadow = true;
        child.receiveShadow = true;
      }
    });
    scene.add(object.scene.children[1]);
    floodLight = new THREE.Object3D();
    floodLight.position.set(-8, 0, 5);
    floodLight.rotation.y = Math.PI / -0.6;
    scene.add(floodLight);
    floodLight.add(object.scene.children[0]);
  });

  const ambient = new THREE.HemisphereLight(0xffffff, 0xaaaa66, 0.35);
  scene.add(ambient);

  //Add lights here
  lights = {};

  // CREATE ROTATING SPOTLIGHT
  lights.rotatingSpot = new THREE.SpotLight(0xffffff, 1, 20, 0.88, 0.5);
  lights.rotatingSpot.position.set(0, 0.35, 5);
  lights.rotatingSpot.castShadow = true;
  lights.rotatingSpot.shadow.camera.near = 3;
  lights.rotatingSpot.shadow.camera.far = 30;
  lights.rotatingSpot.shadow.mapSize.width = 1024;
  lights.rotatingSpot.shadow.mapSize.height = 1024;
  lights.rotatingSpotCameraHelper = new THREE.CameraHelper(
    lights.rotatingSpot.shadow.camera
  );
  lights.rotatingSpotCameraHelper.visible = false;
  scene.add(lights.rotatingSpotCameraHelper);
  lights.rotatingSpotHelper = new THREE.SpotLightHelper(lights.rotatingSpot);
  lights.rotatingSpotHelper.visible = false;
  scene.add(lights.rotatingSpotHelper);
  scene.add(lights.rotatingSpot);

  // CREATE THE FRONT SPOTLIGHT
  lights.frontSpot = new THREE.SpotLight(0xffffff, 1, 20, 0.88, 0.5);
  lights.frontSpot.position.set(0, 0.4, 5.2);
  lights.frontSpot.angle = 1;
  lights.frontSpot.castShadow = true;
  lights.frontSpot.shadow.camera.near = 3;
  lights.frontSpot.shadow.camera.far = 30;
  lights.frontSpot.shadow.mapSize.width = 1024;
  lights.frontSpot.shadow.mapSize.height = 1024;
  lights.frontSpotCameraHelper = new THREE.CameraHelper(
    lights.frontSpot.shadow.camera
  );
  lights.frontSpotCameraHelper.visible = false;
  scene.add(lights.frontSpotCameraHelper);
  lights.frontSpotHelper = new THREE.SpotLightHelper(lights.frontSpot);
  lights.frontSpotHelper.visible = false;
  scene.add(lights.frontSpotHelper);
  scene.add(lights.frontSpot);

  // CREATE THE FLOODLIGHT
  lights.flood = new THREE.DirectionalLight(0xffffff, 0.01);
  lights.flood.position.set(-8, 1.2, 5);
  lights.flood.target.position.set(6, 0, 8);
  lights.flood.rotation.y = Math.PI / -0.6;
  lights.flood.castShadow = true;
  lights.flood.shadow.camera.near = 3;
  lights.flood.shadow.camera.far = 30;
  lights.flood.shadow.mapSize.width = 1024;
  lights.flood.shadow.mapSize.height = 1024;
  lights.floodCameraHelper = new THREE.CameraHelper(lights.flood.shadow.camera);
  lights.floodCameraHelper.visible = false;
  scene.add(lights.floodCameraHelper);
  lights.floodHelper = new THREE.DirectionalLightHelper(lights.flood);
  lights.floodHelper.visible = false;
  scene.add(lights.floodHelper);
  scene.add(lights.flood.target);
  scene.add(lights.flood);

  // CREATE THE TOP SPOTLIGHT
  lights.spot = new THREE.SpotLight(0xffffff, 1, 20, 0.88, 0.5);
  lights.spot.position.set(1, wallsSize, 1);
  lights.spot.castShadow = true;
  lights.spot.shadow.camera.near = 3;
  lights.spot.shadow.camera.far = 30;
  lights.spot.shadow.mapSize.width = 1024;
  lights.spot.shadow.mapSize.height = 1024;
  lights.spotCameraHelper = new THREE.CameraHelper(lights.spot.shadow.camera);
  lights.spotCameraHelper.visible = false;
  scene.add(lights.spotCameraHelper);
  lights.spotHelper = new THREE.SpotLightHelper(lights.spot);
  lights.spotHelper.visible = false;
  scene.add(lights.spotHelper);
  scene.add(lights.spot);

  window.addEventListener("resize", resize, false);

  update();
}

function update() {
  requestAnimationFrame(update);
  renderer.render(scene, camera);

  if (f35) {
    f35.rotation.y += 0.01;
    cylinder.rotation.y += 0.01;

    const lightDTheta = -(2 * Math.PI) / 1000;
    const cylinderDTheta = -(1.5 * -(2 * Math.PI)) / 700;

    cylinderTheta += cylinderDTheta;
    lightTheta += lightDTheta;

    lights.rotatingSpot.position.set(
      5 * Math.cos(cylinderTheta),
      0,
      5 * Math.sin(cylinderTheta)
    );
  }
}

function resize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}
