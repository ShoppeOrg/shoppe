import { IShopItem } from './IShopItem';

export interface IShopData {
  count: number;
  next: string | null;
  previous: string | null;
  results: IShopItem[];
}
