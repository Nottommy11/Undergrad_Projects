let scale = { value: 2 },
  speed = { value: 1 },
  years = { value: 0 },
  earthTheta = 0,
  moonTheta = 0,
  earthRotationCounter = 0;

const yearText = document.querySelector(".year-text");

const sunTexture = "./img/sun.jpg";
const starsTexture = "./img/stars.jpg";
const mercuryTexture = "./img/mercury.jpg";
const venusTexture = "./img/venus.jpg";
const earthTexture = "./img/earth.jpg";
const moonTexture =
  "https://s3-us-west-2.amazonaws.com/s.cdpn.io/17271/lroc_color_poles_1k.jpg";
const displacementURL =
  "https://s3-us-west-2.amazonaws.com/s.cdpn.io/17271/ldem_3_8bit.jpg";
const marsTexture = "./img/mars.jpg";
const jupiterTexture = "./img/jupiter.jpg";
const saturnTexture = "./img/saturn.jpg";
const saturnRingTexture = "./img/saturn ring.png";
const uranusTexture = "./img/uranus.jpg";
const uranusRingTexture = "./img/uranus ring.png";
const neptuneTexture = "./img/neptune.jpg";
const plutoTexture = "./img/pluto.jpg";

init();

function init() {
  const renderer = new THREE.WebGLRenderer();

  renderer.setSize(window.innerWidth, window.innerHeight);

  document.body.appendChild(renderer.domElement);

  const scene = new THREE.Scene();

  const camera = new THREE.PerspectiveCamera(
    45,
    window.innerWidth / window.innerHeight,
    0.1,
    10000
  );

  const orbit = new THREE.OrbitControls(camera, renderer.domElement);

  camera.position.set(-90, 140, 140);
  orbit.update();

  const ambientLight = new THREE.AmbientLight(0x333333);
  scene.add(ambientLight);

  const cubeTextureLoader = new THREE.CubeTextureLoader();
  scene.background = cubeTextureLoader.load([
    starsTexture,
    starsTexture,
    starsTexture,
    starsTexture,
    starsTexture,
    starsTexture,
  ]);

  const textureLoader = new THREE.TextureLoader();

  const displacementMap = textureLoader.load(displacementURL);

  const sunGeo = new THREE.SphereGeometry(scale.value * 16, 30, 30);
  const sunMat = new THREE.MeshBasicMaterial({
    map: textureLoader.load(sunTexture),
  });
  const sun = new THREE.Mesh(sunGeo, sunMat);
  const sunObj = new THREE.Object3D();
  sunObj.add(sun);
  scene.add(sunObj);

  function createPlanet(size, texture, position, ring) {
    /*     const geo = new THREE.SphereGeometry(size, 30, 30);
    const mat = new THREE.MeshStandardMaterial({
      map: textureLoader.load(texture),
    });
    const mesh = new THREE.Mesh(geo, mat);
    const obj = new THREE.Object3D();

    obj.add(mesh);
 */
    /* if (moon) {
      const moonGeo = new THREE.SphereGeometry(moonSize, 30, 30);
      const moonMat = new THREE.MeshPhongMaterial({
        color: 0xffffff,
        map: textureLoader.load(moonTexture),
        displacementMap: displacementMap,
        displacementScale: 0.06,
        bumpMap: displacementMap,
        bumpScale: 0.04,
        reflectivity: 0,
        shininess: 0,
      });
      const moonMesh = new THREE.Mesh(moonGeo, moonMat);
      const moonObj = new THREE.Object3D();
      moonObj.add(moonMesh);
      moonObj.position.x = moonPosition;

      obj.add(moonObj);

      scene.add(obj);
      mesh.position.x = position;
      return { mesh, obj, moonMesh, moonObj };
    }  */

    const geo = new THREE.SphereGeometry(size, 30, 30);
    const mat = new THREE.MeshStandardMaterial({
      map: textureLoader.load(texture),
    });
    const mesh = new THREE.Mesh(geo, mat);
    const obj = new THREE.Object3D();

    obj.add(mesh);

    if (ring) {
      const ringGeo = new THREE.RingGeometry(
        ring.innerRadius,
        ring.outerRadius,
        32
      );
      const ringMat = new THREE.MeshBasicMaterial({
        map: textureLoader.load(ring.texture),
        side: THREE.DoubleSide,
      });
      const ringMesh = new THREE.Mesh(ringGeo, ringMat);

      obj.add(ringMesh);

      ringMesh.position.x = position;
      ringMesh.rotation.x = -0.5 * Math.PI;
    }

    scene.add(obj);
    mesh.position.x = position;
    return { mesh, obj };
  }

  function createMoon(size, texture, position) {
    const geo = new THREE.SphereGeometry(size, 30, 30);
    const mat = new THREE.MeshPhongMaterial({
      color: 0xffffff,
      map: textureLoader.load(texture),
      displacementMap: displacementMap,
      displacementScale: 0.06,
      bumpMap: displacementMap,
      bumpScale: 0.04,
      reflectivity: 0,
      shininess: 0,
    });
    const mesh = new THREE.Mesh(geo, mat);
    const obj = new THREE.Object3D();
    obj.add(mesh);

    scene.add(obj);
    return { mesh, obj };
  }

  const mercury = createPlanet(
    scale.value * 3.2,
    mercuryTexture,
    scale.value * 28
  );
  const venus = createPlanet(scale.value * 5.8, venusTexture, scale.value * 44);

  const earth = createPlanet(scale.value * 6, earthTexture, scale.value * 0);
  const moon = createPlanet(scale.value * 1.5, moonTexture, scale.value * 10);

  const mars = createPlanet(scale.value * 4, marsTexture, scale.value * 78);
  const jupiter = createPlanet(
    scale.value * 12,
    jupiterTexture,
    scale.value * 100
  );
  const saturn = createPlanet(
    scale.value * 10,
    saturnTexture,
    scale.value * 138,
    {
      innerRadius: scale.value * 10,
      outerRadius: scale.value * 20,
      texture: saturnRingTexture,
    }
  );
  const uranus = createPlanet(
    scale.value * 7,
    uranusTexture,
    scale.value * 176,
    {
      innerRadius: scale.value * 7,
      outerRadius: scale.value * 12,
      texture: uranusRingTexture,
    }
  );
  const neptune = createPlanet(
    scale.value * 7,
    neptuneTexture,
    scale.value * 200
  );
  const pluto = createPlanet(
    scale.value * 2.8,
    plutoTexture,
    scale.value * 216
  );

  const pointLight = new THREE.PointLight(0xffffff, 2, scale.value * 300);
  scene.add(pointLight);

  console.log(earth.obj.position.z);

  function animate() {
    //Self-rotation
    sun.rotateY(speed.value * 0.004);
    mercury.mesh.rotateY(speed.value * 0.004);
    venus.mesh.rotateY(speed.value * 0.002);
    earth.mesh.rotateY(speed.value * 0.02);
    mars.mesh.rotateY(speed.value * 0.018);
    jupiter.mesh.rotateY(speed.value * 0.04);
    saturn.mesh.rotateY(speed.value * 0.038);
    uranus.mesh.rotateY(speed.value * 0.03);
    neptune.mesh.rotateY(speed.value * 0.032);
    pluto.mesh.rotateY(speed.value * 0.008);

    moon.mesh.rotateY(speed.value * 0.008);

    //Around-sun-rotation
    mercury.obj.rotateY(speed.value * 0.04);
    venus.obj.rotateY(speed.value * 0.015);
    //earth.obj.rotateY(speed.value * 0.01);
    mars.obj.rotateY(speed.value * 0.008);
    jupiter.obj.rotateY(speed.value * 0.002);
    saturn.obj.rotateY(speed.value * 0.0009);
    uranus.obj.rotateY(speed.value * 0.0004);
    neptune.obj.rotateY(speed.value * 0.0001);
    pluto.obj.rotateY(speed.value * 0.00007);

    moon.obj.rotateY(speed.value * 0.02);

    const earthR = scale.value * 62;
    const EarthDTheta = (speed.value * -(2 * Math.PI)) / 700;

    cylinderTheta += EarthDTheta;
    earth.obj.position.set(
      earthR * Math.cos(cylinderTheta),
      0,
      earthR * Math.sin(cylinderTheta)
    );

    const moonR = scale.value * 0;
    const moonDTheta = (speed.value * -(2 * Math.PI)) / 1000;

    lightTheta += moonDTheta;
    moon.obj.position.set(
      earthR * Math.cos(cylinderTheta) + moonR * moonR * Math.cos(lightTheta),
      0,
      earthR * Math.sin(cylinderTheta) + moonR * moonR * Math.sin(lightTheta)
    );

    if (earth.obj.position.x < 0.1 && earth.obj.position.x > -0.1) {
      earthRotationCounter++;

      console.log("Earth is at 0");
      if (earthRotationCounter % 2 == 1 && earthRotationCounter != 1) {
        years.value++;
        yearText.innerText = "Earth Years: " + years.value;
      }
    }

    renderer.render(scene, camera);
  }

  renderer.setAnimationLoop(animate);

  window.addEventListener("resize", function () {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  /*   function updatePlanetScale() {
    // sun.mesh.scale.set(scale.value, scale.value, scale.value);
    mercury.mesh.scale.set(scale.value, scale.value, scale.value);
    venus.mesh.scale.set(scale.value, scale.value, scale.value);
    earth.mesh.scale.set(scale.value, scale.value, scale.value);
    mars.mesh.scale.set(scale.value, scale.value, scale.value);
    jupiter.mesh.scale.set(scale.value, scale.value, scale.value);
    saturn.mesh.scale.set(scale.value, scale.value, scale.value);
    uranus.mesh.scale.set(scale.value, scale.value, scale.value);
    neptune.mesh.scale.set(scale.value, scale.value, scale.value);
    pluto.mesh.scale.set(scale.value, scale.value, scale.value);
  } */

  /*   function updatePlanetPosition() {
    mercury.obj.position.x = scale.value * 28;
    venus.obj.position.x = scale.value * 44;
    earth.obj.position.x = scale.value * 62;
    mars.obj.position.x = scale.value * 78;
    jupiter.obj.position.x = scale.value * 100;
    saturn.obj.position.x = scale.value * 138;
    uranus.obj.position.x = scale.value * 176;
    neptune.obj.position.x = scale.value * 200;
    pluto.obj.position.x = scale.value * 216;
  } */

  const gui = new dat.GUI();

  gui
    .add(speed, "value", 0.1, 10)
    .name("Speed")
    .onChange(function (value) {
      speed.value = value;
    });

  /*   gui
    .add(scale, "value", 0.1, 10)
    .name("Scale")
    .onChange(function (value) {
      scale.value = value;
      updatePlanetScale();
      updatePlanetPosition();
    }); */
}
