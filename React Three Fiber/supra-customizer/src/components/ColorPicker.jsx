import React from "react"
import { SketchPicker } from "react-color"
import { useSnapshot } from "valtio"

import state from "../store"

const ColorPicker = ({ props }) => {
  const snap = useSnapshot(state)

  return (
    <SketchPicker
      className={"color-picker-" + props}
      color={snap[props]}
      disableAlpha
      onChange={(color) => (state[props] = color.hex)}
    />
  )
}

export default ColorPicker
