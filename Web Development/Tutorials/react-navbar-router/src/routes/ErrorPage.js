import { useRouteError } from "react-router-dom";

export default function ErrorPage() {
  const error = useRouteError();
  console.error(error);

  return (
    <div id="error-page">
      <h1>OOOOF!</h1>
      <p>This page does not exist!</p>
      <p>
        <i>{error.statusText || error.message}</i>
      </p>
    </div>
  );
}
