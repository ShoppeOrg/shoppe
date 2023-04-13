import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { InfiniteScrollModule } from 'ngx-infinite-scroll';
import { CarouselModule } from 'ngx-owl-carousel-o';

// import { NgxMaterialRatingModule } from 'ngx-material-rating';
import { FormsModule } from '@angular/forms';



import { ShopRoutingModule } from './shop-routing.module';
import { ShopComponent } from './pages/shop/shop.component';
import { SharedModule } from '../../shared/shared.module';
import { ShopFilterComponent } from './components/shop-filter/shop-filter.component';
import { ShopListComponent } from './components/shop-list/shop-list.component';
import { ShopItemComponent } from './components/shop-item/shop-item.component';
import { MaterialModule } from '../../material.module';
import {ReactiveFormsModule} from '@angular/forms';
import { ShopDetailsComponent } from './pages/shop-details/shop-details.component';

@NgModule({
  declarations: [
    ShopComponent,
    ShopFilterComponent,
    ShopListComponent,
    ShopItemComponent,
    ShopDetailsComponent,

  ],
  imports: [
    CommonModule,
    ShopRoutingModule,
    SharedModule,
    MaterialModule,
    InfiniteScrollModule,
    ReactiveFormsModule,
    CarouselModule,
    FormsModule,
    // NgxMaterialRatingModule,

  ],
  providers: [],
})
export class ShopModule {}
