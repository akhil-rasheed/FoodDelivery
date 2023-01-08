export default {
  getCart() {
    let obj = JSON.parse(localStorage.getItem("cart"));
    if (obj) {
      return obj;
    } else return [];
  },

  addItem(item) {
    let obj = this.getCart();
    obj.push({ item: { ...item }, quantity: 1 });
    localStorage.setItem("cart", JSON.stringify(obj));
    return obj;
  },

  removeItem(itemId) {
    let obj = JSON.parse(localStorage.getItem("cart"));
    let newObj = obj.filter((item) => item.itemId != itemId);
    localStorage.setItem("cart", JSON.stringify(newObj));
  },
};
