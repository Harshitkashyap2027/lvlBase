// lvlBase Bento Grid Drag & Drop
const BentoDrag = {
  dragItem: null,
  dragSource: null,
  
  init(containerSelector = '.bento-grid') {
    const grids = document.querySelectorAll(containerSelector);
    grids.forEach(grid => this.initGrid(grid));
  },
  
  initGrid(grid) {
    const items = grid.querySelectorAll('.bento-item');
    items.forEach(item => {
      item.setAttribute('draggable', 'true');
      item.addEventListener('dragstart', (e) => this.onDragStart(e));
      item.addEventListener('dragend', (e) => this.onDragEnd(e));
      item.addEventListener('dragover', (e) => this.onDragOver(e));
      item.addEventListener('drop', (e) => this.onDrop(e));
    });
  },
  
  onDragStart(e) {
    this.dragItem = e.target;
    this.dragSource = e.target.parentNode;
    e.target.style.opacity = '0.4';
    e.dataTransfer.effectAllowed = 'move';
  },
  
  onDragEnd(e) {
    e.target.style.opacity = '1';
    document.querySelectorAll('.bento-item').forEach(i => i.classList.remove('drag-over'));
  },
  
  onDragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    e.currentTarget.classList.add('drag-over');
  },
  
  onDrop(e) {
    e.preventDefault();
    if (e.currentTarget !== this.dragItem) {
      const parent = e.currentTarget.parentNode;
      const afterEl = this.getDragAfterElement(parent, e.clientY);
      if (!afterEl) parent.appendChild(this.dragItem);
      else parent.insertBefore(this.dragItem, afterEl);
    }
    this.saveLayout();
  },
  
  getDragAfterElement(container, y) {
    const elements = [...container.querySelectorAll('.bento-item:not(.dragging)')];
    return elements.reduce((closest, child) => {
      const box = child.getBoundingClientRect();
      const offset = y - box.top - box.height / 2;
      return (offset < 0 && offset > closest.offset) ? { offset, element: child } : closest;
    }, { offset: Number.NEGATIVE_INFINITY }).element;
  },
  
  saveLayout() {
    const grid = document.querySelector('.bento-grid');
    if (!grid) return;
    const order = [...grid.children].map(el => el.dataset.id || el.className);
    localStorage.setItem('bento-layout', JSON.stringify(order));
  }
};

export default BentoDrag;
