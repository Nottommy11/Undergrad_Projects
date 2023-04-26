import { Stats, OrbitControls, Center, Environment } from "@react-three/drei"
import { Canvas } from "@react-three/fiber"
import { useSnapshot } from "valtio"
import {
  EffectComposer,
  DepthOfField,
  Noise,
  Bloom
} from "@react-three/postprocessing"

import Car from "./components/Car"
import CameraRig from "./components/CameraRig"
import store from "./store"
import ColorPicker from "./components/ColorPicker"
import hdrUrl from "./assets/autoshop_01_4k.hdr"

export default function App() {
  const snap = useSnapshot(store)

  function getRGB(c) {
    return parseInt(c, 16) || c
  }

  function getsRGB(c) {
    return getRGB(c) / 255 <= 0.03928
      ? getRGB(c) / 255 / 12.92
      : Math.pow((getRGB(c) / 255 + 0.055) / 1.055, 2.4)
  }

  function getLuminance(hexColor) {
    return (
      0.2126 * getsRGB(hexColor.substr(1, 2)) +
      0.7152 * getsRGB(hexColor.substr(3, 2)) +
      0.0722 * getsRGB(hexColor.substr(-2))
    )
  }

  function getContrast(f, b) {
    const L1 = getLuminance(f)
    const L2 = getLuminance(b)
    return (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05)
  }

  function getTextColor(bgColor) {
    const whiteContrast = getContrast(bgColor, "#ffffff")
    const blackContrast = getContrast(bgColor, "#000000")

    return whiteContrast > blackContrast ? "#ffffff" : "#000000"
  }

  return (
    <>
      <Canvas camera={[0, 0, 0]} shadows gl={{ preserveDrawingBuffer: true }}>
        <CameraRig>
          <Center>
            <Car shadows castShadow receiveShadow />
          </Center>
        </CameraRig>
        {snap.orbitControls ? <OrbitControls autoRotate /> : null}

        <ambientLight intensity={0.1} />
        <EffectComposer>
          <DepthOfField
            focusDistance={0}
            focalLength={0.02}
            bokehScale={2}
            height={480}
          />
          <Bloom luminanceThreshold={0} luminanceSmoothing={0.9} height={300} />
          <Noise opacity={0.02} />
        </EffectComposer>
        <Environment files={hdrUrl} background={true} />
        <Stats />
      </Canvas>
      <div
        className="edit-body"
        style={{
          backgroundColor: snap.body,
          color: getTextColor(snap.body)
        }}>
        <h2>Body</h2>
      </div>
      <ColorPicker props={"body"} />
      <div
        className="edit-accent"
        style={{
          backgroundColor: snap.accent,
          color: getTextColor(snap.accent)
        }}>
        <h2>Accent</h2>
      </div>
      <ColorPicker props={"accent"} />
      <div
        className="edit-interior"
        style={{
          backgroundColor: snap.interior,
          color: getTextColor(snap.interior)
        }}>
        <h2>Interior</h2>
      </div>
      <ColorPicker props={"interior"} />
      <div
        className="orbit-controls"
        onClick={() => {
          !snap.orbitControls
            ? (store.orbitControls = true)
            : (store.orbitControls = false)
        }}
        style={{
          backgroundColor: snap.body,
          color: getTextColor(snap.body)
        }}>
        <h2>
          Orbit
          <br />
          Controls
        </h2>
      </div>
    </>
  )
}
