import React, { useRef } from "react"
import { useFrame } from "@react-three/fiber"
import { easing } from "maath"
import { useSnapshot } from "valtio"

import state from "../store"

const CameraRig = ({ children }) => {
  const group = useRef()
  const snap = useSnapshot(state)

  useFrame((state, delta) => {
    // set the initial position of the model
    let targetPosition = [0, 0.4, 2]

    snap.orbitControls
      ? easing.dampE(group.current.rotation, [0, 0, 0])
      : setCam()

    // set model camera position
    function setCam() {
      easing.damp3(state.camera.position, targetPosition, 0.25, delta)

      // set the model rotation smoothly
      easing.dampE(
        group.current.rotation,
        [state.pointer.y / 3, -state.pointer.x / 2, 0],
        0.25,
        delta
      )
    }
  })

  return <group ref={group}>{children}</group>
}

export default CameraRig
