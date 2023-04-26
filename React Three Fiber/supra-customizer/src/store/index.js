import { proxy } from "valtio"

const state = proxy({
  body: "#9D5800",
  accent: "#000",
  interior: "#603E00",
  orbitControls: false
})

export default state
