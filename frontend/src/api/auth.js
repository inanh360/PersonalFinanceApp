import api from "./axios";

export const login = async (email, password) => {
  const res = await api.post("dj-rest-auth/login/", { email, password });
  return res.data;
};

export const register = async (email, password1, password2) => {
  const res = await api.post("dj-rest-auth/registration/", {
    email,
    password1,
    password2,
  });
  return res.data;
};

export const logout = async () => {
  await api.post("dj-rest-auth/logout/");
};
