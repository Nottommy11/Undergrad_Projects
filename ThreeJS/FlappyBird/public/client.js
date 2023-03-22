/**
 * Work based on the Three JS Ocean examples at
 * https://threejs.org/examples/?q=water#webgl_shaders_ocean
 */
import * as THREE from "three";
//import { OrbitControls } from "./jsm/controls/OrbitControls.js";
import Stats from "./jsm/libs/stats.module.js";
//import { GUI } from "./jsm/libs/lil-gui.module.min.js";
import { Water } from "./jsm/objects/Water.js";
import { Sky } from "./jsm/objects/Sky.js";
import { GLTFLoader } from "./jsm/loaders/GLTFLoader.js";

const scene = new THREE.Scene();

let birdMixer,
  frogMixer,
  clock,
  bird,
  frog,
  birdAction,
  frogAction,
  hits = 0,
  gameOver = false,
  score = 0,
  highScore = 0;

clock = new THREE.Clock();

// Load high score from local storage
function loadHighScore() {
  let json = localStorage.getItem("highscore");
  if (json) {
    let data = JSON.parse(json);
    highScore = data.highscore;
  }
}

loadHighScore();

// Save high score to local storage
function saveHighScore() {
  let data = {
    highscore: score,
  };
  let json = JSON.stringify(data);
  localStorage.setItem("highscore", json);
}

const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.set(150, 100, 0);
camera.lookAt(0, 100, 0);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

/* const controls = new OrbitControls(camera, renderer.domElement);
controls.maxPolarAngle = Math.PI * 0.495;
controls.target.set(0, 10, 0);
controls.minDistance = 40.0;
controls.maxDistance = 200.0; */

const sun = new THREE.Vector3();
const waterGeometry = new THREE.PlaneGeometry(10000, 10000);
const water = new Water(waterGeometry, {
  textureWidth: 512,
  textureHeight: 512,
  waterNormals: new THREE.TextureLoader().load(
    "textures/waternormals.jpg",
    function (texture) {
      texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
    }
  ),
  alpha: 1.0,
  sunDirection: new THREE.Vector3(),
  sunColor: 0xffffff,
  waterColor: 0x001e0f,
  distortionScale: 3.7,
  fog: scene.fog !== undefined,
});
water.rotation.x = -Math.PI / 2;

water.receiveShadow = true;

scene.add(water);

const sky = new Sky();
sky.scale.setScalar(10000);
scene.add(sky);

let uniforms = sky.material.uniforms;
uniforms["turbidity"].value = 10;
uniforms["rayleigh"].value = 2;
uniforms["mieCoefficient"].value = 0.005;
uniforms["mieDirectionalG"].value = 0.8;

const parameters = {
  inclination: 0.45,
  azimuth: 0.35,
};

const pmremGenerator = new THREE.PMREMGenerator(renderer);
pmremGenerator.compileEquirectangularShader();

function updateSun() {
  let theta = Math.PI * (parameters.inclination - 0.5);
  let phi = 2 * Math.PI * (parameters.azimuth - 0.5);

  sun.x = Math.cos(phi);
  sun.y = Math.sin(phi) * Math.sin(theta);
  sun.z = Math.sin(phi) * Math.cos(theta);

  sky.material.uniforms["sunPosition"].value.copy(sun);
  water.material.uniforms["sunDirection"].value.copy(sun).normalize();

  scene.environment = pmremGenerator.fromScene(sky).texture;
}

updateSun();

window.addEventListener(
  "resize",
  () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    render();
  },
  false
);

const stats = Stats();
document.body.appendChild(stats.dom);

// Load the bird model
// https://discourse.threejs.org/t/easiest-way-to-play-skeletal-animation-from-gltf/7792/4
const loader = new GLTFLoader();
loader.load("./Models/low_poly_bird_animated/scene.gltf", function (gltf) {
  birdMixer = new THREE.AnimationMixer(gltf.scene);
  birdAction = birdMixer.clipAction(gltf.animations[0]);
  birdAction.timeScale = 10;

  birdAction.setLoop(THREE.LoopOnce);

  bird = gltf.scene;
  bird.scale.set(4, 4, 4);
  bird.position.set(0, 80, 0);

  gltf.scene.castShadow = true;
  gltf.scene.receiveShadow = true;

  scene.add(gltf.scene);
});

// Add a listener to the spacebar to make the bird fly
// https://stackoverflow.com/questions/42958252/how-do-i-move-a-three-js-cube-with-keyboard-input
// https://threejs.org/docs/?q=animation#api/en/animation/AnimationAction
document.addEventListener("keydown", onDocumentKeyDown, false);
function onDocumentKeyDown(event) {
  let keyCode = event.which;
  // Spacebar
  if (keyCode == 32) {
    bird.position.y += 16;
    birdAction.play();
    birdAction.reset();
  }
}

// Create pipes
const pipeGeometry = new THREE.CylinderGeometry(10, 10, 100, 64);
const pipeMaterial = new THREE.MeshStandardMaterial({ color: 0x00ff00 });

// Create array of bottom pipes
const pipesBottom = [];

for (let i = 0; i < 25; i++) {
  // Generate random height for pipe
  const pipeHeight = Math.floor(Math.random() * 40) - 15;

  const pipe = new THREE.Mesh(pipeGeometry, pipeMaterial);
  pipe.position.set(0, pipeHeight, i * 25);

  pipesBottom.push(pipe);
}

// Add pipes to scene
pipesBottom.forEach((pipe) => {
  pipe.castShadow = true;
  pipe.receiveShadow = true;

  scene.add(pipe);
});

// Create array of top pipes
const pipesTop = [];

for (let i = 0; i < 25; i++) {
  // Generate random height for pipe
  const pipeHeight = Math.floor(Math.random() * 40) + 160;

  const pipe = new THREE.Mesh(pipeGeometry, pipeMaterial);
  pipe.position.set(0, pipeHeight, i * 25);

  pipesTop.push(pipe);
}

// Add pipes to scene
pipesTop.forEach((pipe) => {
  pipe.castShadow = true;
  pipe.receiveShadow = true;

  scene.add(pipe);
});

// Load the frog model
loader.load("./Models/cursed_frog_attack/scene.gltf", function (gltf) {
  frogMixer = new THREE.AnimationMixer(gltf.scene);
  frogAction = frogMixer.clipAction(gltf.animations[0]);
  frogAction.timeScale = 1;
  frogAction.play();

  frog = gltf.scene;
  frog.position.set(0, -300, 0);
  frog.rotateY(Math.PI);
  frog.scale.set(2, 2, 2);

  gltf.scene.castShadow = true;
  gltf.scene.receiveShadow = true;

  scene.add(gltf.scene);
});

new (function animate() {
  let delta = clock.getDelta();

  if (birdMixer) birdMixer.update(delta);
  if (frogMixer) frogMixer.update(delta);

  if (bird && bird.position.y >= 0) bird.position.y -= 0.4;
  requestAnimationFrame(animate);
  render();

  // Move Bottom pipes
  pipesBottom.forEach((pipe) => {
    pipe.position.z -= 0.5;
    if (pipe.position.z < -275) {
      pipe.position.z = 350;
      pipe.position.y = Math.floor(Math.random() * 40) - 15;
    }

    if (bird && !gameOver) {
      // Check for collision
      if (
        bird.position.z >= pipe.position.z - 5 &&
        bird.position.z <= pipe.position.z + 5 &&
        bird.position.y >= pipe.position.y - 50 &&
        bird.position.y <= pipe.position.y + 50
      ) {
        console.log("hit");
        hits++;
      }

      // Add score
      if (
        bird.position.z >= pipe.position.z - 5 &&
        bird.position.z <= pipe.position.z + 5
      ) {
        score++;
        console.log(score);
      }
    }
  });

  // Move Top pipes
  pipesTop.forEach((pipe) => {
    pipe.position.z -= 0.5;
    if (pipe.position.z < -275) {
      pipe.position.z = 350;
      pipe.position.y = Math.floor(Math.random() * 40) + 160;
    }

    if (bird && !gameOver) {
      // Check for collision
      if (
        bird.position.z >= pipe.position.z - 5 &&
        bird.position.z <= pipe.position.z + 5 &&
        bird.position.y >= pipe.position.y - 50 &&
        bird.position.y <= pipe.position.y + 50
      ) {
        console.log("hit");
        hits++;
      }
    }
  });

  // Gamer Over
  if (hits >= 5 && !gameOver) {
    frog.position.y = 0;
    console.log("Game Over");
    gameOver = true;

    // Display Game Over
    const gameOverText = document.createElement("div");
    gameOverText.style.position = "absolute";
    gameOverText.style.width = 1;
    gameOverText.style.height = 1;
    gameOverText.style.color = "white";
    gameOverText.style.fontSize = "100px";
    gameOverText.style.top = 50 + "%";
    gameOverText.style.left = 50 + "%";
    gameOverText.style.transform = "translate(-50%, -50%)";
    gameOverText.innerHTML = "Game Over";
    document.body.appendChild(gameOverText);

    // Display Score
    const scoreText = document.createElement("div");
    scoreText.style.position = "absolute";
    scoreText.style.width = 1;
    scoreText.style.height = 1;
    scoreText.style.color = "white";
    scoreText.style.fontSize = "100px";
    scoreText.style.top = 70 + "%";
    scoreText.style.left = 50 + "%";
    scoreText.style.transform = "translate(-50%, -50%)";
    scoreText.innerHTML = "Score: " + score;
    document.body.appendChild(scoreText);

    // Display High Score
    const highScoreText = document.createElement("div");
    highScoreText.style.position = "absolute";
    highScoreText.style.width = 1;
    highScoreText.style.height = 1;
    highScoreText.style.color = "white";
    highScoreText.style.fontSize = "100px";
    highScoreText.style.top = 90 + "%";
    highScoreText.style.left = 50 + "%";
    highScoreText.style.transform = "translate(-50%, -50%)";
    highScoreText.innerHTML = "High Score: " + highScore;
    document.body.appendChild(highScoreText);

    // Save High Score
    if (score > highScore) {
      saveHighScore();
    }

    // Remove spacebar listener
    document.removeEventListener("keydown", onDocumentKeyDown, false);
  }

  stats.update();
})();

function render() {
  water.material.uniforms["time"].value += 1.0 / 60.0;

  renderer.render(scene, camera);
}

/* // Add axis helper
// https://threejs.org/docs/#api/en/helpers/AxisHelper
const axesHelper = new THREE.AxesHelper(10);
scene.add(axesHelper);
 */
