import { Component, OnInit } from '@angular/core';

import { ShopService } from '../../services/shop.service';
import { IQuery } from '../../interfaces/IQuery';
import { map } from 'rxjs';
import { FilterShopService } from '../../services/filter-shop.service';
import { IShopItem } from '../../interfaces/IShopItem';

@Component({
  selector: 'app-shop-list',
  templateUrl: './shop-list.component.html',
  styleUrls: ['./shop-list.component.scss'],
})
export class ShopListComponent implements OnInit {
  disableScroll = true;
  products: Array<IShopItem> = [];
  count!: number;

  searchQuery: IQuery = {
    page_size: 12,
    page: 1,
    filterChanged: false,
  };

  constructor(
    private shopService: ShopService,
    private filterShopService: FilterShopService,
  ) {}

  ngOnInit(): void {
    this.filterShopService.productsSubject.subscribe((data: IQuery) => {
      this.getProducts(data);
    });
  }

  getMoreProducts(): void {
    this.searchQuery.page++;

    this.filterShopService.setQuery(this.searchQuery);
  }

  getProducts(searchQuery: IQuery): void {
    this.shopService
      .getProducts(searchQuery)
      .pipe(
        map(data => {
          this.count = data.count;
          return data.results;
        }),
      )
      .subscribe(res => {
        if (searchQuery.filterChanged) {

          this.disableScroll = true;
          this.products = res;
          return;
        }
        this.products = [...this.products, ...res];
      });
  }

  enableScroll(): void {
    this.disableScroll = false;
  }

  shouldInfiniteScrollDisable(): boolean {
    return this.disableScroll || this.products.length >= this.count;
  }
}
