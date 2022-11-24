export default function validateInfo(values) {
  let errors = {};

  if (!values.username.trim()) {
    errors.username = "Username Required";
  }

  if (!values.email.trim()) {
    errors.email = "Email Required";
  } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)) {
    errors.email = "Email Address is Invalid";
  }

  if (!values.password.trim()) {
    errors.password = "Password is Required";
  } else if (values.password.length < 8) {
    errors.password = "Password Must be at Least 8 Characters";
  }

  if (!values.password2) {
    errors.password2 = "Password is Required";
  } else if (values.password2 !== values.password) {
    errors.password2 = "Passwords do Not Match";
  }

  return errors;
}
