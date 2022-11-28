import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
	* {
		@import url("https://fonts.googleapis.com/css?family=Roboto&display=swap");
		margin: 0;
		padding: 0;
		box-sizing: border-box;
		font-family: "Roboto";
		font-family: Open-"Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande", "Lucida Sans", Arial, sans-serif;
	}
`;

export default GlobalStyle;
