export class ShopItem {
  constructor(
    public created_at: Date,
    public description: string,
    public id: number,
    public in_stock: boolean,
    public name: string,
    public price: string,
    public quantity: number,
    public updated_at: Date,
    public url: string,
    public amount: number = 1,
    public main_image: string,
  ) {}
}
