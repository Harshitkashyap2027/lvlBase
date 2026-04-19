// lvlBase SPA Router
const Router = {
  routes: {},
  currentRoute: null,
  
  register(path, handler, roles = []) {
    this.routes[path] = { handler, roles };
  },
  
  navigate(path, pushState = true) {
    const route = this.routes[path] || this.routes['*'];
    if (!route) return console.warn('No route for:', path);
    
    const user = this.getCurrentUser();
    if (route.roles.length > 0 && user && !route.roles.includes(user.role)) {
      return this.navigate('/auth/blocked.html');
    }
    
    if (pushState) history.pushState({ path }, '', path);
    this.currentRoute = path;
    route.handler(path);
  },
  
  getCurrentUser() {
    try { return JSON.parse(localStorage.getItem('lvlbase_user')); }
    catch { return null; }
  },
  
  init() {
    window.addEventListener('popstate', (e) => {
      if (e.state?.path) this.navigate(e.state.path, false);
    });
    this.navigate(window.location.pathname, false);
  }
};

export default Router;
