import { Component, OnInit } from '@angular/core';
 import { IconsService } from 'src/app/shared/services/icons.service';
@Component({
  selector: 'app-shop-item',
  templateUrl: './shop-item.component.html',
  styleUrls: ['./shop-item.component.scss']
})
export class ShopItemComponent implements OnInit {

  constructor(private readonly iconService: IconsService) {
    this.iconService.addIcons();
  }

  ngOnInit(): void {
  }

}
