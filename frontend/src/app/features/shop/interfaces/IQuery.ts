export interface IQuery {
  page: number;
  page_size: number;
  min_price?: number;
  max_price?: number;
  order_by?: string;
  in_stock?: boolean;
  filterChanged: boolean;
}
