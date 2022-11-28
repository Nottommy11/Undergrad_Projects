import React from "react";
import Header from "../components/Header";
import Hero from "../components/Hero";
import image from "../img/img-2.jpg";
import { motion } from "framer-motion";
import { animationTwo } from "../animations/index";

function About() {
  return (
    <motion.div initial="out" animate="in" exit="out" variants={animationTwo}>
      <Header />
      <Hero image={image} title="About" desc="Look at this reptilian" />
    </motion.div>
  );
}

export default About;
