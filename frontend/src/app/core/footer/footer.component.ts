import { Component, OnInit } from '@angular/core';
import { IconsService } from '../../shared/services/icons.service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {
  // constructor(private readonly iconService: IconsService) {
  //   this.iconService.addIcons();
  // }

  ngOnInit(): void {}
}
