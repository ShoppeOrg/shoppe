import { Component, OnDestroy, OnInit } from '@angular/core';
import { map, ReplaySubject, takeUntil } from 'rxjs';

import { ShopService } from '../../services/shop.service';
import { IQuery } from '../../interfaces/IQuery';
import { FilterShopService } from '../../services/filter-shop.service';
import { IShopItem } from '../../../../shared/interfaces/IShopItem';
import { ShopItem } from '../../../../shared/classes/ShopItem';

@Component({
  selector: 'app-shop-list',
  templateUrl: './shop-list.component.html',
  styleUrls: ['./shop-list.component.scss'],
})
export class ShopListComponent implements OnInit, OnDestroy {
  private destroyed$: ReplaySubject<boolean> = new ReplaySubject(1);

  disableScroll = true;
  products: Array<IShopItem> = [];
  count!: number;
  searchQuery: IQuery;

  constructor(
    private shopService: ShopService,
    private filterShopService: FilterShopService,
  ) {
    this.searchQuery = { ...this.filterShopService.initialQuery };
  }

  ngOnInit(): void {
    this.filterShopService.productsSubject
      .pipe(takeUntil(this.destroyed$))
      .subscribe((data: IQuery) => {
        this.getProducts(data);
      });
  }

  ngOnDestroy(): void {
    this.destroyed$.next(true);
    this.destroyed$.complete();
    this.filterShopService.setQuery({ ...this.filterShopService.initialQuery });
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
          this.products = res.map(
            item =>
              new ShopItem(
                item.created_at,
                item.description,
                item.id,
                item.in_stock,
                item.name,
                item.price,
                item.quantity,
                item.updated_at,
                item.url,
                item.amount,
                item.main_image,
              ),
          );
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
