import React from "react";
import Header from "../components/Header";
import Hero from "../components/Hero";
import image from "../img/img-1.jpg";
import { motion } from "framer-motion";
import { animationOne, transition } from "../animations/index";

function Home() {
  return (
    <motion.div
      initial="out"
      animate="in"
      exit="out"
      variants={animationOne}
      transition={transition}
    >
      <Header />
      <Hero image={image} title="Home" desc=" Look at this birb" />
    </motion.div>
  );
}

export default Home;
