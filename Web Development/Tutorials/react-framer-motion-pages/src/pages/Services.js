import React from "react";
import Header from "../components/Header";
import Hero from "../components/Hero";
import image from "../img/img-3.jpg";
import { motion } from "framer-motion";
import { animationThree } from "../animations/index";

function Services() {
  return (
    <motion.div
      initial="out"
      animate="end"
      exit="out"
      variants={animationThree}
    >
      <Header />
      <Hero image={image} title="Services" desc="Look at this birb" />
    </motion.div>
  );
}

export default Services;
