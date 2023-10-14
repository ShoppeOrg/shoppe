import { Injectable } from '@angular/core';
import { IShopItem } from '../interfaces/IShopItem';

@Injectable({
  providedIn: 'root',
})
export class CartService {
  private shopList: Array<IShopItem> = [];

  constructor() {}

  getProducts(): Array<IShopItem> {
    return this.shopList;
  }

  saveCart(): void {
    localStorage.setItem('cart_items', JSON.stringify(this.shopList));
  }

  addToCart(shopItem: IShopItem): void {
    this.loadCart();
    console.log('cart', this.shopList)
    const selectedItemIndex = this.findShopItemIndex(shopItem);
    if (selectedItemIndex > -1) {
      this.shopList[selectedItemIndex] = {
        ...this.shopList[selectedItemIndex],
        amount: this.shopList[selectedItemIndex].amount + shopItem.amount,
      };
    } else {
      this.shopList.push(shopItem);
    }
    this.saveCart();
  }

  loadCart(): void {
    this.shopList =
      JSON.parse(localStorage.getItem('cart_items') as string) || [];
  }

  removeShopItem(shopItem: IShopItem): void {
    const index = this.shopList.findIndex(
      (prod: IShopItem) => prod.id === shopItem.id,
    );

    if (index > -1) {
      this.shopList.splice(index, 1);
      this.saveCart();
    }
  }

  findShopItemIndex(shopItem: IShopItem): number {
    return this.shopList.findIndex((x: IShopItem) => x.id === shopItem.id);
  }

  updateCart(shopList: Array<IShopItem>): void {
    localStorage.setItem('cart_items', JSON.stringify(shopList));
  }

  getTotal(): number {
    return this.shopList.reduce(
      (sum, product) => ({
        quantity: 1,
        price: sum.price + product.amount * +product.price,
      }),
      { quantity: 1, price: 0 },
    ).price;
  }
}
