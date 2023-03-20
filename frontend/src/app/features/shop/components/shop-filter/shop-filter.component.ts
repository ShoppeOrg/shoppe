import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { debounceTime } from 'rxjs';
import { FilterShopService } from '../../services/filter-shop.service';

@Component({
  selector: 'app-shop-filter',
  templateUrl: './shop-filter.component.html',
  styleUrls: ['./shop-filter.component.scss'],
})
export class ShopFilterComponent implements OnInit {
  filterForm: FormGroup;
  minPrice = 0;
  maxPrice = 10000;
  sortOptions = ['popular.desc', 'price.asc', 'price.desc', 'recent.desc'];

  constructor(private filterShopService: FilterShopService) {
    this.filterForm = new FormGroup({
      search: new FormControl({ value: '', disabled: true }),
      order_by: new FormControl(''),
      in_stock: new FormControl(true),
      min_price: new FormControl(this.minPrice),
      max_price: new FormControl(this.maxPrice),
    });
  }

  ngOnInit() {
    this.filterForm.valueChanges.pipe(debounceTime(300)).subscribe(val => {
      this.filterShopService.setQuery({ ...val, filterChanged: true, page: 1 });
    });
  }
}
