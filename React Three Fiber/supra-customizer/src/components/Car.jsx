import React from "react"
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader"
import { useLoader } from "@react-three/fiber"
import { useSnapshot } from "valtio"

import store from "../store"
import carUrl from "../assets/toyota_gr_supra.glb"

function Car() {
  const snap = useSnapshot(store)

  const gltf = useLoader(GLTFLoader, carUrl)

  gltf.scene.children[0].children[0].children[0].children[8].children[3].children[0].material.color.set(
    snap.accent
  )
  gltf.scene.children[0].children[0].children[0].children[8].children[4].children[0].material.color.set(
    snap.body
  )
  gltf.scene.children[0].children[0].children[0].children[8].children[20].children[0].material.color.set(
    snap.accent
  )
  gltf.scene.children[0].children[0].children[0].children[8].children[33].children[0].material.color.set(
    snap.interior
  )
  gltf.scene.children[0].children[0].children[0].children[1].children[0].children[0].material.color.set(
    snap.accent
  )
  gltf.scene.children[0].children[0].children[0].children[3].children[0].children[0].material.color.set(
    snap.accent
  )

  gltf.scene.children[0].children[0].children[0].children[8].children.forEach(
    (mesh) => {
      mesh.children[0].castShadow = true
    }
  )

  gltf.scene.children[0].children[0].children[0].children.forEach((child) => {
    child.children[0].children.forEach((mesh) => {
      mesh.castShadow = true
    })
  })

  console.log(gltf.scene)

  return (
    <primitive
      object={gltf.scene}
      position={[0, 1, 0]}
      rotation={[0, Math.PI / 2, 0]}
      scale={0.5}
    />
  )
}

export default Car
