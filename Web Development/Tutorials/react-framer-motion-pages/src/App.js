// YouTube Tutorial
// https://youtu.be/WHCr554UJ1I
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Services from "./pages/Services";
import { AnimatePresence } from "framer-motion";
import "./App.css";
import styled from "styled-components";

const Section = styled.section`
  overflow-x: hidden;
`;

const router = createBrowserRouter([
  {
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/about",
        element: <About />,
      },
      {
        path: "/services",
        element: <Services />,
      },
    ],
  },
]);

function App() {
  return (
    <>
      <Section>
        <AnimatePresence exitBeforeEnter>
          <RouterProvider router={router} />
        </AnimatePresence>
      </Section>
    </>
  );
}

export default App;
